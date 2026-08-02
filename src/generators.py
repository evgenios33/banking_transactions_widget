from typing import Generator, Iterator


def filter_by_currency(transactions_data: list[dict], currency_code: str) -> Iterator[dict]:
    """Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    for transaction in transactions_data:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions_data: list[dict]) -> Generator[str, None, None]:
    """Возвращает описание каждой операции по очереди."""
    for transaction in transactions_data:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генерирует номера банковских карт в заданном диапазоне."""
    if not (1 <= start <= 9999999999999999 and 1 <= stop <= 9999999999999999):
        raise ValueError("Укажите число от 1 до 9999999999999999")

    if stop < start:
        raise ValueError("Начальное значение не может быть больше конечного.")

    for num in range(start, stop + 1):
        card_num_str = f"{start:016}"
        formatted_card_num = " ".join([card_num_str[i: i + 4] for i in range(0, len(card_num_str), 4)])
        yield formatted_card_num
        start += 1
