import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def find_cyrillic_letters(type_and_num: str) -> bool:
    """Проверяет вхождение русских букв в строку."""
    return bool(re.search("[а-яА-Я]", type_and_num))


def mask_account_card(type_and_num: str) -> str:
    """Обрабатывает информацию о банковских картах и счетах
    и возвращает строку с замаскированным номером в нужном формате."""
    if type_and_num == "":
        incorrect_input = """Некорректный ввод! Введите данные в формате:
1. Для банковских карт - тип продукта на английском языке и 16-значный номер карты
(Пример: Visa Platinum 7000792289606361).
2. Для банковского счета - слово "Счет" и 20-значный номер счета
(Пример: Счет 73654108430135874305)."""
        return incorrect_input
    elif find_cyrillic_letters(type_and_num):
        list_of_substr = type_and_num.strip().rsplit(" ", 1)
        type_product = "".join(list_of_substr[0])
        account_num = "".join(list_of_substr[-1])
        mask_account_num = get_mask_account(int(account_num))
        result = type_product + " " + mask_account_num
        return result
    else:
        list_of_substr = type_and_num.strip().rsplit(" ", 1)
        type_product = "".join(list_of_substr[0])
        card_num = "".join(list_of_substr[-1])
        mask_card_num = get_mask_card_number(int(card_num))
        result = type_product + " " + mask_card_num
        return result


def get_date(date: str) -> str:
    """Возвращает строку с датой в формате "ДД.ММ.ГГГГ"."""
    iso_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date_format = iso_date.strftime("%d.%m.%Y")
    return new_date_format
