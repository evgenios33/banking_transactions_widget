import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


def test_process_bank_search(list_of_dict_with_transactions: list[dict]) -> None:
    result = process_bank_search(list_of_dict_with_transactions, "с карты")
    assert result == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]


def test_process_bank_search_empty(list_of_dict_with_transactions: list[dict]) -> None:
    result = process_bank_search(list_of_dict_with_transactions, "")
    assert result == []


def test_process_bank_search_empty_data() -> None:
    data = []  # type: ignore
    result = process_bank_search(data, "с карты")
    assert result == []


def test_process_bank_operations(
    list_of_dict_with_transactions: list[dict], list_categories_for_test: list[str]
) -> None:
    result = process_bank_operations(list_of_dict_with_transactions, list_categories_for_test)
    assert result == {
        "Перевод организации": 2,
        "Перевод с карты на карту": 1,
        "Открытие вклада": 0,
        "Перевод со счета на счет": 2,
    }


def test_process_bank_operations_empty_data(list_categories_for_test: list[str]) -> None:
    data = []  # type: ignore
    result = process_bank_operations(data, list_categories_for_test)
    assert result == {
        "Перевод организации": 0,
        "Перевод с карты на карту": 0,
        "Открытие вклада": 0,
        "Перевод со счета на счет": 0,
    }


def test_process_bank_operations_empty_categories(list_of_dict_with_transactions: list[dict]) -> None:
    categories = []  # type: ignore
    result = process_bank_operations(list_of_dict_with_transactions, categories)
    assert result == {}


@pytest.mark.parametrize("state_value", ["EXECUTED", "CANCELED", "ACTIVE", "INACTIVE", "PENDING"])
def test_filter_by_state(list_of_dict_for_state: list[dict], state_value: str) -> None:
    assert filter_by_state(list_of_dict_for_state, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428835, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(list_of_dict_for_state, "INACTIVE") == [
        {"id": 74628835, "state": "INACTIVE", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226111, "state": "INACTIVE", "date": "2018-09-12T21:27:25.241689"},
    ]
    assert filter_by_state(list_of_dict_for_state, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert filter_by_state(list_of_dict_for_state, "ACTIVE") == [
        {"id": 939719456, "state": "ACTIVE", "date": "2018-06-30T02:08:58.425572"},
        {"id": 354626727, "state": "ACTIVE", "date": "2018-09-12T21:27:25.241689"},
    ]
    assert filter_by_state(list_of_dict_for_state, "PENDING") == [
        {"id": 615068573, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
        {"id": 364064591, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
    ]

    with pytest.raises(ValueError) as exc_info:
        filter_by_state([], "")
        filter_by_state(list_of_dict_for_state, "FAILED")

        assert str(exc_info.value) == "Некорректный ввод. Ключ 'state' не найден или значение отсутствует."


def test_sort_by_date_true(list_of_dict_for_date: list[dict]) -> None:
    assert sort_by_date(list_of_dict_for_date, True) == [
        {"id": 615064591, "state": "CANCELED", "date": "2026-10-17T08:21:33.419441"},
        {"id": 74628835, "state": "INACTIVE", "date": "2025-07-11T18:35:29.512364"},
        {"id": 354626727, "state": "ACTIVE", "date": "2025-02-13T21:27:25.241689"},
        {"id": 615068573, "state": "PENDING", "date": "2024-10-14T08:21:33.419441"},
        {"id": 594226111, "state": "INACTIVE", "date": "2022-09-12T21:27:25.241689"},
        {"id": 41428835, "state": "EXECUTED", "date": "2020-03-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-10-05T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-01-15T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719456, "state": "ACTIVE", "date": "2015-06-30T02:08:58.425572"},
        {"id": 364064591, "state": "PENDING", "date": "2013-10-25T08:21:33.419441"},
    ]


def test_sort_by_date_false(list_of_dict_for_date: list[dict]) -> None:
    assert sort_by_date(list_of_dict_for_date, False) == [
        {"id": 364064591, "state": "PENDING", "date": "2013-10-25T08:21:33.419441"},
        {"id": 939719456, "state": "ACTIVE", "date": "2015-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-01-15T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-10-05T08:21:33.419441"},
        {"id": 41428835, "state": "EXECUTED", "date": "2020-03-03T18:35:29.512364"},
        {"id": 594226111, "state": "INACTIVE", "date": "2022-09-12T21:27:25.241689"},
        {"id": 615068573, "state": "PENDING", "date": "2024-10-14T08:21:33.419441"},
        {"id": 354626727, "state": "ACTIVE", "date": "2025-02-13T21:27:25.241689"},
        {"id": 74628835, "state": "INACTIVE", "date": "2025-07-11T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2026-10-17T08:21:33.419441"},
    ]

    with pytest.raises(KeyError) as exc_info:
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED"},
                {"id": 594226727, "state": "CANCELED", "date": "12-09-2018T21:27:25"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 615064592, "state": "CANCELED", "date": "2018-02-30T08:21:33"},
            ],
            True,
        )
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED"},
                {"id": 594226727, "state": "CANCELED", "date": "12-09-2018T21:27:25"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 615064592, "state": "CANCELED", "date": "2018-02-30T08:21:33"},
            ],
            False,
        )

        assert str(exc_info.value) == "Ключ 'date' отсутствует в словаре."

    with pytest.raises(ValueError) as exc_info:
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29"},
                {"id": 594226727, "state": "CANCELED", "date": "12-09-2018T21:27:25"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33"},
                {"id": 615064592, "state": "CANCELED", "date": "2018-02-30T08:21:33"},
            ],
            True,
        )

        assert str(exc_info.value) == "Некорректный формат даты в словаре."
