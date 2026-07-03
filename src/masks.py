def get_mask_card_number(card_num: int) -> str:
    """Принимает на вход номер карты и возвращает ее маску в формате 1234 56** **** 7890."""
    # Преобразуем номер карты в строку.
    str_card_num = str(card_num)
    # Создаем новую строку с помощью срезов и конкатенации.
    card_num_mask = str_card_num[:4] + " " + str_card_num[4:6] + "** **** " + str_card_num[-4:]
    # Возвращаем новую строку.
    return card_num_mask


def get_mask_account(account_num: int) -> str:
    """Принимает на вход номер счета и возвращает его маску в формате **7890."""
    # Преобразуем номер счета в строку.
    str_account_num = str(account_num)
    # Создаем новую строку с помощью срезов и конкатенации.
    account_num_mask = "**" + str_account_num[-4:]
    # Возвращаем новую строку.
    return account_num_mask
