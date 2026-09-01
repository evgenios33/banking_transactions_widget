import json
import logging
import os

utils_logger = logging.getLogger(__name__)
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="a", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


def read_data_from_json(file_path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        utils_logger.warning(f"Файл пуст или не найден по указанному пути: {file_path}")
        return []

    try:
        with open(file_path) as f:
            operations_data = json.load(f)
            if isinstance(operations_data, list):
                utils_logger.info("Данные успешно получены.")
                return operations_data
            utils_logger.warning("Файл не содержит список.")
    except json.JSONDecodeError as ex:
        utils_logger.error(f"Произошла ошибка: {ex}")
    return []
