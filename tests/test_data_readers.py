from unittest.mock import mock_open, patch

import pandas as pd

from src.data_readers import read_data_from_csv, read_data_from_xlsx


def test_read_data_csv_success() -> None:
    """Тест успешного чтения CSV-файла с данными."""
    csv_content = "id;amount;currency_code\n1;100;RUB\n2;200;USD\n3;300;EUR\n"

    with patch("builtins.open", mock_open(read_data=csv_content)) as mock_file:
        with patch("os.path.isfile", return_value=True):
            with patch("os.path.getsize", return_value=len(csv_content)):
                result = read_data_from_csv("/fake/path/test_file.csv")

                assert len(result) == 3
                assert result[0] == {"id": "1", "amount": "100", "currency_code": "RUB"}
                assert result[1] == {"id": "2", "amount": "200", "currency_code": "USD"}
                assert result[2] == {"id": "3", "amount": "300", "currency_code": "EUR"}
                assert result == [
                    {"id": "1", "amount": "100", "currency_code": "RUB"},
                    {"id": "2", "amount": "200", "currency_code": "USD"},
                    {"id": "3", "amount": "300", "currency_code": "EUR"},
                ]
                mock_file.assert_called_once_with("/fake/path/test_file.csv")  # , mode="r", encoding=None


def test_read_data_csv_file_not_found() -> None:
    """Тест, когда файл не найден (FileNotFoundError)."""
    with patch("os.path.isfile", return_value=False):
        try:
            read_data_from_csv("/fake/path/nonexistent.csv")
            assert False, "Ожидалось исключение FileNotFoundError"
        except FileNotFoundError as e:
            assert "Файл не найден" in str(e)


def test_read_data_csv_empty_file() -> None:
    """Тест, когда файл существует, но пустой (ValueError)."""
    with patch("os.path.isfile", return_value=True):
        with patch("os.path.getsize", return_value=0):
            try:
                read_data_from_csv("empty.csv")
                assert False, "Ожидалось исключение ValueError"
            except ValueError as e:
                assert "Файл пуст" in str(e)


def test_read_data_excel_success() -> None:
    """Тест успешного чтения данных: проверяем, что pandas.read_excel вызывается корректно."""
    mock_file_path = "/fake/path/dummy_path.xlsx"

    mock_df = pd.DataFrame(
        [
            {"id": 1, "amount": 100, "currency_code": "RUB"},
            {"id": 2, "amount": 200, "currency_code": "USD"},
            {"id": 3, "amount": 300, "currency_code": "EUR"},
        ]
    )
    expected_result = mock_df.to_dict(orient="records")

    with patch("pandas.read_excel", return_value=mock_df) as mock_read:
        with patch("os.path.isfile", return_value=True) as mock_isfile:
            with patch("os.path.getsize", return_value=1024) as mock_getsize:
                result = read_data_from_xlsx(mock_file_path)

                assert result == expected_result
                mock_isfile.assert_called_once_with(mock_file_path)
                mock_getsize.assert_called_once_with(mock_file_path)
                mock_read.assert_called_once_with(mock_file_path)


def test_read_data_excel_file_not_found() -> None:
    """Тест на отсутствие файла: проверяем, что выбрасывается FileNotFoundError."""
    mock_file_path = "/fake/path/non_existent_file.xlsx"

    with patch("os.path.isfile", return_value=False) as mock_isfile:
        try:
            read_data_from_xlsx(mock_file_path)
            assert False, "Ожидалось исключение FileNotFoundError"
        except FileNotFoundError as e:
            assert str(e) == f"Файл не найден по указанному пути: {mock_file_path}"
            mock_isfile.assert_called_once_with(mock_file_path)


def test_read_data_excel_empty_file() -> None:
    """Тест на пустой файл: проверяем, что выбрасывается ValueError."""
    mock_file_path = "/fake/path/empty_file.xlsx"

    with patch("os.path.isfile", return_value=True) as mock_isfile:
        with patch("os.path.getsize", return_value=0) as mock_getsize:
            try:
                read_data_from_xlsx(mock_file_path)
                assert False, "Ожидалось исключение ValueError"
            except ValueError as e:
                assert str(e) == f"Файл пуст: {mock_file_path}"
                mock_isfile.assert_called_once_with(mock_file_path)
                mock_getsize.assert_called_once_with(mock_file_path)
