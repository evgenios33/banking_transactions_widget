import logging

masks_logger = logging.getLogger(__name__)
masks_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="a", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_num: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску в формате 1234 56** **** 7890."""
    formatted_card_num = card_num.replace(" ", "")

    if len(formatted_card_num) != 16:
        masks_logger.error("Некорректный ввод. Введите 16-значный номер карты.")
        raise ValueError("Некорректный ввод. Введите 16-значный номер карты.")

    if not formatted_card_num.isdigit():
        masks_logger.error("Некорректный ввод. Номер карты не может содержать буквы.")
        raise ValueError("Некорректный ввод. Номер карты не может содержать буквы.")

    card_num_mask = formatted_card_num[:4] + " " + formatted_card_num[4:6] + "** **** " + formatted_card_num[-4:]
    masks_logger.info("Номер карты успешно замаскирован.")
    return card_num_mask


def get_mask_account(account_num: str) -> str:
    """Принимает на вход номер счета и возвращает его маску в формате **7890."""
    formatted_account_num = account_num.replace(" ", "")
    if len(formatted_account_num) != 20:
        masks_logger.error("Некорректный ввод. Введите 20-значный номер счета.")
        raise ValueError("Некорректный ввод. Введите 20-значный номер счета.")

    if not formatted_account_num.isdigit():
        masks_logger.error("Некорректный ввод. Номер счета не может содержать буквы.")
        raise ValueError("Некорректный ввод. Номер счета не может содержать буквы.")

    account_num_mask = "**" + formatted_account_num[-4:]
    masks_logger.info("Номер счета успешно замаскирован.")
    return account_num_mask
