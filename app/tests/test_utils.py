import pytest

from app.utils.utils import compute_file_hash


def test_compute_file_hash_returns_string_for_valid_file(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("hello world", encoding="utf-8")

    file_hash = compute_file_hash(test_file)

    assert isinstance(file_hash, str)
    assert len(file_hash) == 64  # SHA-256 hex digest length


def test_compute_file_hash_same_file_same_hash(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("same content", encoding="utf-8")

    first_hash = compute_file_hash(test_file)
    second_hash = compute_file_hash(test_file)

    assert first_hash == second_hash


def test_compute_file_hash_different_files_different_hashes(tmp_path):
    file_a = tmp_path / "a.txt"
    file_b = tmp_path / "b.txt"

    file_a.write_text("content A", encoding="utf-8")
    file_b.write_text("content B", encoding="utf-8")

    assert compute_file_hash(file_a) != compute_file_hash(file_b)


def test_compute_file_hash_detects_small_content_change(tmp_path):
    file_a = tmp_path / "a.txt"
    file_b = tmp_path / "b.txt"

    file_a.write_text("hello world", encoding="utf-8")
    file_b.write_text("hello worle", encoding="utf-8")

    assert compute_file_hash(file_a) != compute_file_hash(file_b)


def test_compute_file_hash_empty_file_has_valid_hash(tmp_path):
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("", encoding="utf-8")

    file_hash = compute_file_hash(empty_file)

    assert isinstance(file_hash, str)
    assert len(file_hash) == 64


def test_compute_file_hash_missing_file_raises_error(tmp_path):
    missing_file = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        compute_file_hash(missing_file)