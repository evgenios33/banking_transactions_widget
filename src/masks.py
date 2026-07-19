def get_mask_card_number(card_num: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску в формате 1234 56** **** 7890."""
    formatted_card_num = card_num.replace(" ", "")

    if len(formatted_card_num) != 16:
        raise ValueError("Некорректный ввод. Введите 16-значный номер карты.")

    if not formatted_card_num.isdigit():
        raise ValueError("Некорректный ввод. Номер карты не может содержать буквы.")

    card_num_mask = formatted_card_num[:4] + " " + formatted_card_num[4:6] + "** **** " + formatted_card_num[-4:]
    return card_num_mask


def get_mask_account(account_num: str) -> str:
    """Принимает на вход номер счета и возвращает его маску в формате **7890."""
    formatted_account_num = account_num.replace(" ", "")
    if len(formatted_account_num) != 20:
        raise ValueError("Некорректный ввод. Введите 20-значный номер счета.")

    if not formatted_account_num.isdigit():
        raise ValueError("Некорректный ввод. Номер счета не может содержать буквы.")

    account_num_mask = "**" + formatted_account_num[-4:]
    return account_num_mask
