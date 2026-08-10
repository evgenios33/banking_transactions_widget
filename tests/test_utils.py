import json
from unittest.mock import mock_open, patch

from src.utils import convert_json_file


def test_empty_file() -> None:
    with patch("os.path.isfile", return_value=True), patch("os.path.getsize", return_value=0):
        result = convert_json_file("dummy_path.json")
        assert result == []


def test_nonexistent_file() -> None:
    with patch("os.path.isfile", return_value=False):
        result = convert_json_file("dummy_path.json")
        assert result == []


def test_invalid_json() -> None:
    fake_file = mock_open(read_data="not a json")
    with (
        patch("builtins.open", fake_file),
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=10),
    ):
        result = convert_json_file("dummy_path.json")
        assert result == []


def test_valid_list_of_dicts() -> None:
    data = [{"amount": 100}, {"amount": 200}]
    json_data = json.dumps(data)
    fake_file = mock_open(read_data=json_data)
    with (
        patch("builtins.open", fake_file),
        patch("os.path.isfile", return_value=True),
        patch("os.path.getsize", return_value=50),
    ):
        result = convert_json_file("dummy_path.json")
        assert result == data
