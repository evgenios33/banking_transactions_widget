import math
import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def find_cyrillic_letters(type_and_num: str) -> bool:
    """Проверяет вхождение русских букв в строку."""
    return bool(re.search("[а-яА-Я]", type_and_num))


def mask_account_card(type_and_num: str) -> str:
    """Обрабатывает информацию о банковских картах и счетах
    и возвращает строку с замаскированным номером в нужном формате."""
    if type_and_num is None:
        return ""

    if isinstance(type_and_num, float):
        if math.isnan(type_and_num):
            return ""
        type_and_num = str(type_and_num).rstrip(".0")

    type_and_num = str(type_and_num).strip()
    if not type_and_num:
        return ""

    if type_and_num.startswith("Счет ") and len(type_and_num) >= 25:
        list_of_substr = type_and_num.strip().rsplit(" ", 1)
        type_product = "".join(list_of_substr[0])
        account_num = "".join(list_of_substr[-1])
        mask_account_num = get_mask_account(account_num)
        result = type_product + " " + mask_account_num
        return result

    elif len(type_and_num.split()) >= 2:
        list_of_substr = type_and_num.strip().rsplit(" ", 1)
        type_product = "".join(list_of_substr[0])
        card_num = "".join(list_of_substr[-1])
        mask_card_num = get_mask_card_number(card_num)
        result = type_product + " " + mask_card_num
        return result

    else:
        raise ValueError("""Некорректный ввод! Введите данные в формате:
            1. Для банковских карт - тип продукта на английском языке и 16-значный номер карты
            (Пример: Visa Platinum 7000792289606361).
            2. Для банковского счета - слово "Счет" и 20-значный номер счета
            (Пример: Счет 73654108430135874305).""")


def get_date(date: str) -> str:
    """Возвращает строку с датой в формате "ДД.ММ.ГГГГ"."""
    formatted_date = date.strip()

    allowed_formats = ["%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S"]

    for format_ in allowed_formats:
        try:
            iso_date = datetime.strptime(formatted_date, format_)
            return iso_date.strftime("%d.%m.%Y")
        except ValueError:
            continue

    raise ValueError("Некорректный формат даты!")
