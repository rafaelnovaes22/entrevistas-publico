"""Contratos executáveis dos cinco exercícios e da execução local."""

import contextlib
import io
import json
import sqlite3
import unittest
from pathlib import Path

from exercicios.sql.praticar import build_database, execute_query, main

ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "exercicios" / "sql" / "referencias"


def reference_query(number: int) -> str:
    return (REFERENCES / f"q{number}.sql").read_text(encoding="utf-8")


class SqlPracticeTests(unittest.TestCase):
    def test_conversion_filters_year_and_minimum_volume(self) -> None:
        _, rows = execute_query(reference_query(1))
        self.assertEqual(
            rows,
            [
                ("Seguradora Alfa", 6, 4, 66.7),
                ("Seguradora Beta", 6, 3, 50.0),
                ("Seguradora Gama", 4, 2, 50.0),
            ],
        )

    def test_latest_quotes(self) -> None:
        _, rows = execute_query(reference_query(2))
        self.assertEqual(
            rows,
            [
                ("Cliente Alfa", 127000, "2026-05-15"),
                ("Cliente Beta", 180000, "2026-02-10"),
                ("Cliente Delta", 160000, "2026-03-18"),
                ("Cliente Epsilon", 210000, "2026-06-28"),
                ("Cliente Gama", 88000, "2026-06-12"),
                ("Cliente Zeta", 101000, "2026-05-08"),
            ],
        )

    def test_policies_without_claims(self) -> None:
        _, rows = execute_query(reference_query(3))
        self.assertEqual(
            rows,
            [
                (3, "Cliente Gama", 82000),
                (5, "Cliente Epsilon", 90000),
                (6, "Cliente Zeta", 101000),
                (8, "Cliente Gama", 88000),
                (9, "Cliente Epsilon", 210000),
            ],
        )

    def test_top_two_claims(self) -> None:
        _, rows = execute_query(reference_query(4))
        self.assertEqual(
            rows,
            [
                (1, 1, 35000),
                (1, 2, 12000),
                (2, 3, 80000),
                (4, 4, 5000),
                (7, 5, 22000),
                (10, 6, 40000),
            ],
        )

    def test_running_premium(self) -> None:
        _, rows = execute_query(reference_query(5))
        self.assertEqual(len(rows), 10)
        self.assertEqual(
            [row[3] for row in rows],
            [
                115000,
                235000,
                362000,
                250000,
                140000,
                90000,
                300000,
                82000,
                170000,
                101000,
            ],
        )

    def test_latest_quote_tie_uses_larger_identifier(self) -> None:
        connection = build_database()
        try:
            connection.execute(
                "INSERT INTO quotes VALUES (17, 13, 130000, '2026-05-15')"
            )
            rows = connection.execute(reference_query(2)).fetchall()
            self.assertEqual(rows[0], ("Cliente Alfa", 130000, "2026-05-15"))
        finally:
            connection.close()

    def test_top_claim_tie_uses_larger_identifier(self) -> None:
        connection = build_database()
        try:
            connection.execute(
                "INSERT INTO claims VALUES (8, 1, '2026-06-20', 12000, 'open')"
            )
            rows = connection.execute(reference_query(4)).fetchall()
            self.assertEqual(rows[:2], [(1, 1, 35000), (1, 8, 12000)])
        finally:
            connection.close()

    def test_database_is_recreated_for_each_query(self) -> None:
        first = execute_query("SELECT COUNT(*) FROM submissions")
        self.assertEqual(first, execute_query("SELECT COUNT(*) FROM submissions"))
        self.assertEqual(first[1], [(20,)])

    def test_writes_and_external_databases_are_denied(self) -> None:
        queries = [
            "DELETE FROM clients",
            "DROP TABLE quotes",
            "ATTACH DATABASE ':memory:' AS other",
            "PRAGMA query_only = OFF",
        ]
        for query in queries:
            with self.subTest(query=query), self.assertRaises(sqlite3.DatabaseError):
                execute_query(query)

    def test_multiple_statements_are_denied(self) -> None:
        with self.assertRaises(sqlite3.ProgrammingError):
            execute_query("SELECT 1; SELECT 2;")

    def test_invalid_sql_is_rejected(self) -> None:
        with self.assertRaises(sqlite3.OperationalError):
            execute_query("SELECT missing FROM clients")

    def test_cli_prints_json(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = main([str(REFERENCES / "q1.sql")])
        self.assertEqual(status, 0)
        self.assertEqual(json.loads(output.getvalue())["event"], "query_completed")

    def test_cli_missing_file_returns_failure(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = main([str(REFERENCES / "inexistente.sql")])
        self.assertEqual(status, 1)
        self.assertEqual(json.loads(output.getvalue())["event"], "query_failed")


if __name__ == "__main__":
    unittest.main()
