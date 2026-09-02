"""Execute uma consulta de treino em um banco sintético, somente em memória."""

import argparse
import json
import sqlite3
from collections.abc import Sequence
from pathlib import Path

SCHEMA_PATH = Path(__file__).with_name("schema.sql")
READ_OPERATIONS = {sqlite3.SQLITE_SELECT, sqlite3.SQLITE_READ, sqlite3.SQLITE_FUNCTION}
SqlValue = str | int | float | bytes | None


def authorize_read(
    operation: int,
    argument: str | None,
    second_argument: str | None,
    database: str | None,
    trigger: str | None,
) -> int:
    # Restringe o laboratório a consultas, inclusive quando o SQL vem de outro arquivo.
    return sqlite3.SQLITE_OK if operation in READ_OPERATIONS else sqlite3.SQLITE_DENY


def build_database() -> sqlite3.Connection:
    connection = sqlite3.connect(":memory:")
    connection.execute("PRAGMA foreign_keys = ON")
    connection.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    return connection


def execute_query(query: str) -> tuple[list[str], list[tuple[SqlValue, ...]]]:
    connection = build_database()
    connection.set_authorizer(authorize_read)
    try:
        cursor = connection.execute(query)
        if cursor.description is None:
            raise ValueError("Consulta sem colunas; esperado um SELECT com resultados.")
        columns = [column[0] for column in cursor.description]
        return columns, cursor.fetchall()
    finally:
        connection.close()


def query_failure(file_path: Path, error: Exception) -> dict[str, str]:
    return {
        "event": "query_failed",
        "file": str(file_path),
        "error": str(error),
        "expected": "Arquivo UTF-8 com um SELECT válido",
    }


def main(arguments: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("consulta", type=Path, help="Arquivo .sql com um SELECT")
    options = parser.parse_args(arguments)
    try:
        query = options.consulta.read_text(encoding="utf-8-sig")
        columns, rows = execute_query(query)
        result = {"event": "query_completed", "columns": columns, "rows": rows}
    except (OSError, UnicodeError, sqlite3.Error, ValueError) as error:
        print(json.dumps(query_failure(options.consulta, error)))
        return 1
    print(json.dumps(result, ensure_ascii=True, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
