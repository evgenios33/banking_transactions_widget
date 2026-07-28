import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("code_value", ["USD", "RUB"])
def test_filter_by_currency(list_of_dict_with_transactions: list[dict], code_value: str) -> None:
    usd_transactions = filter_by_currency(list_of_dict_with_transactions, "USD")
    assert next(usd_transactions) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_transactions) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(usd_transactions) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    rub_transactions = filter_by_currency(list_of_dict_with_transactions, "RUB")
    assert next(rub_transactions) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(rub_transactions) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


@pytest.mark.parametrize("code_value", ["USD", "RUB", "EURO"])
def test_filter_by_currency_no_currency(list_of_dict_with_transactions: list[dict], code_value: str) -> None:
    no_currency_gen = filter_by_currency(list_of_dict_with_transactions, "EURO")
    with pytest.raises(StopIteration) as exc_info:
        next(no_currency_gen)

        assert str(exc_info.value) == "Отсутствуют транзакции в заданной валюте."


def test_filter_by_currency_empty_list() -> None:
    empty_list_gen = filter_by_currency([], "")
    with pytest.raises(StopIteration) as exc_info:
        next(empty_list_gen)

        assert str(exc_info.value) == "Передан пустой список или ключ 'code' не найден."


def test_transaction_descriptions(list_of_dict_with_transactions: list[dict]) -> None:
    gen = transaction_descriptions(list_of_dict_with_transactions)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод с карты на карту"
    assert next(gen) == "Перевод организации"


#
def test_transaction_descriptions_empty_list() -> None:
    empty_list_gen = transaction_descriptions([])
    with pytest.raises(StopIteration) as exc_info:
        next(empty_list_gen)

        assert str(exc_info.value) == "Передан пустой список."


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (20, 23, ["0000 0000 0000 0020", "0000 0000 0000 0021", "0000 0000 0000 0022", "0000 0000 0000 0023"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list[tuple]) -> None:
    gen = list(card_number_generator(start, stop))
    assert gen == expected


@pytest.mark.parametrize(
    "start, stop, expected",
    [(1, 1, ["0000 0000 0000 0001"]), (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"])],
)
def test_card_number_generator_extreme_values(start: int, stop: int, expected: list[tuple]) -> None:
    gen = list(card_number_generator(start, stop))
    assert gen == expected
