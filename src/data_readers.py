import csv
import os

import pandas as pd


def read_data_from_csv(file_path: str) -> list[dict]:
    """Функция принимает путь к файлу CSV, считывает информацию и возвращает список словарей с данными."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл не найден по указанному пути: {file_path}")

    if os.path.getsize(file_path) == 0:
        raise ValueError(f"Файл пуст: {file_path}")

    with open(file_path) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        data_list = []
        for row in reader:
            data_list.append(row)

        return data_list


if __name__ == "__main__":
    result = read_data_from_csv("/Users/evgenios_33/PycharmProjects/banking_transactions_widget/data/transactions.csv")
    print(result)


def read_data_from_xlsx(file_path: str) -> list[dict]:
    """Функция принимает путь к файлу Excel, считывает информацию и возвращает список словарей с данными."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл не найден по указанному пути: {file_path}")

    if os.path.getsize(file_path) == 0:
        raise ValueError(f"Файл пуст: {file_path}")

    df = pd.read_excel(file_path)
    data_list = df.to_dict(orient="records")
    return data_list


# if __name__ == '__main__':
#     print(read_data_from_xlsx("/Users/evgenios_33/PycharmProjects/banking_transactions_widget/data/transactions_excel.xlsx"))
