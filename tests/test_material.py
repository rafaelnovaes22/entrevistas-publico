"""Verifica a navegação do material e o uso após baixar o repositório."""

import csv
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def public_documents() -> list[Path]:
    documents = list(ROOT.glob("*.md"))
    for directory in ("guias", "modelos", "exercicios"):
        documents.extend((ROOT / directory).rglob("*.md"))
    return documents


def local_links(document: Path) -> list[Path]:
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", document.read_text(encoding="utf-8"))
    return [
        (document.parent / link.split("#")[0]).resolve()
        for link in links
        if not link.startswith(("https://", "http://", "#"))
    ]


class PublicMaterialTests(unittest.TestCase):
    def test_document_links_stay_in_the_public_repository_and_exist(self) -> None:
        targets = [
            target
            for document in public_documents()
            for target in local_links(document)
        ]
        self.assertGreater(len(targets), 10)
        for target in targets:
            with self.subTest(path=str(target)):
                self.assertTrue(target.is_relative_to(ROOT))
                self.assertTrue(target.is_file())

    def test_documents_have_no_email_phone_or_local_user_path(self) -> None:
        patterns = [
            r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}",
            r"\+55\s*\(?\d{2}\)?[\s-]*\d{4,5}[\s-]*\d{4}",
            r"(?i)[a-z]:[\\/]Users[\\/]",
            r"/home/[^/\s]+/",
        ]
        contents = "\n".join(
            document.read_text(encoding="utf-8") for document in public_documents()
        )
        for pattern in patterns:
            with self.subTest(pattern=pattern):
                self.assertIsNone(re.search(pattern, contents))

    def test_tracking_template_contains_headers_only(self) -> None:
        with (ROOT / "modelos" / "acompanhamento.csv").open(
            encoding="utf-8", newline=""
        ) as template:
            rows = list(csv.reader(template))
        self.assertEqual(len(rows), 1)
        self.assertEqual(len(rows[0]), 9)

    def test_cli_works_outside_the_project_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            result = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "exercicios/sql/praticar.py"),
                    str(ROOT / "exercicios/sql/resposta.sql"),
                ],
                cwd=temporary_directory,
                capture_output=True,
                text=True,
                timeout=10,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(json.loads(result.stdout)["rows"]), 6)


if __name__ == "__main__":
    unittest.main()
