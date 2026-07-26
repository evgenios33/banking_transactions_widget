import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "type_and_num, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card(type_and_num: str, expected: str) -> None:
    assert mask_account_card(type_and_num) == expected

    with pytest.raises(ValueError) as exc_info:
        mask_account_card("")
        mask_account_card("Visa 1234")

        assert str(exc_info.value) == """Некорректный ввод! Введите данные в формате:
        1. Для банковских карт - тип продукта на английском языке и 16-значный номер карты
        (Пример: Visa Platinum 7000792289606361).
        2. Для банковского счета - слово "Счет" и 20-значный номер счета
        (Пример: Счет 73654108430135874305)."""


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2021-01-01T01:01:01.010101", "01.01.2021"),
        ("2022-02-02T02:02:02.02020", "02.02.2022"),
        ("2023-03-03T03:03:03.0303", "03.03.2023"),
        ("2024-04-04T04:04:04.040", "04.04.2024"),
        ("2025-05-05T05:05:05.05", "05.05.2025"),
        ("2026-06-06T06:06:06.6", "06.06.2026"),
    ],
)
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected

    with pytest.raises(ValueError) as exc_info:
        get_date("")
        get_date("2024-03-11T02:26:18")
        get_date("2024-03-11T02:26:18.")

        assert str(exc_info.value) == "Некорректный ввод. Введите дату в формате '%Y-%m-%dT%H:%M:%S.%f'."
