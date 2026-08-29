import re
from collections import Counter
from datetime import datetime


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Принимает список словарей с данными и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    descriptions = [operation["description"] for operation in data]
    counted = Counter(descriptions)
    result = {category: counted[category] for category in categories}
    return result


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Принимает список словарей с данными и строку поиска, а возвращает список словарей,
    у которых в описании есть данная строка."""
    if not search or not search.strip():
        print("Вы ничего не ввели.")
        return []

    pattern = re.compile(re.escape(search.strip()), flags=re.IGNORECASE)

    result = []
    for item in data:
        description = item.get("description", "Описание отсутствует")
        if pattern.search(description):
            result.append(item)

    return result


def filter_by_state(data: list[dict], state_value: str = "EXECUTED") -> list[dict]:
    """Возвращает новый список словарей, содержащий только те словари,
    у которых ключ "state" соответствует переданному значению."""
    if not data:
        raise ValueError("Некорректный ввод. Ключ 'state' не найден или значение отсутствует.")

    filter_list = [item for item in data if item.get("state", "") == state_value.upper().strip()]
    return filter_list


def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    """Возвращает новый список отсортированный по ключу "date"."""
    allowed_formats = ["%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S"]

    for item in data:
        if "date" not in item:
            raise KeyError(f"Ключ 'date' отсутствует в словаре: {item}.")

        date_val = item["date"]
        if not isinstance(date_val, str):
            raise ValueError(f"Значение 'date' должно быть строкой: {item}")

        valid = False
        for format_ in allowed_formats:
            try:
                datetime.strptime(date_val, format_)
                valid = True
                break
            except ValueError:
                continue

        if not valid:
            raise ValueError(f"Некорректный формат даты в словаре: {item}")

    return sorted(data, key=lambda x: x["date"], reverse=descending)
