import json
import os


def convert_json_file(file_path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        return []

    try:
        with open(file_path) as f:
            operations_data = json.load(f)
            if isinstance(operations_data, list):
                return operations_data
    except json.JSONDecodeError:
        print("Invalid JSON data.")

    return []
