import pytest

from app.ingestion.file_loader import file_loader


def test_file_loader_returns_from_txt(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("hello world", encoding="utf-8")

    file_hash = file_loader(test_file)

    assert len(file_hash) == 1 

