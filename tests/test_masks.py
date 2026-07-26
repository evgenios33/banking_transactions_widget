import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_num, expected",
    [
        ("1234567887654321", "1234 56** **** 4321"),
        ("1234 5678 8765 4321", "1234 56** **** 4321"),
        ("  1234567887654321  ", "1234 56** **** 4321"),
    ],
)
def test_get_mask_card_number(card_num: str, expected: str) -> None:
    assert get_mask_card_number(card_num) == expected

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
        get_mask_card_number("01234567899876543210")

        assert str(exc_info.value) == "Некорректный ввод. Введите 16-значный номер карты."

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("OI23456789OI2345")

        assert str(exc_info.value) == "Некорректный ввод. Номер карты не может содержать буквы."


@pytest.mark.parametrize(
    "account_num, expected",
    [
        ("01234567899876543210", "**3210"),
        ("0123 4567 8998 7654 3210", "**3210"),
        ("  01234567899876543210  ", "**3210"),
    ],
)
def test_get_mask_account(account_num: str, expected: str) -> None:
    assert get_mask_account(account_num) == expected

    with pytest.raises(ValueError) as exc_info:
        get_mask_account("")
        get_mask_account("012345678909876543210")

        assert str(exc_info.value) == "Некорректный ввод. Введите 20-значный номер счета."

    with pytest.raises(ValueError) as exc_info:
        get_mask_account("OI2345678998765432IO")

        assert str(exc_info.value) == "Некорректный ввод. Номер счета не может содержать буквы."
