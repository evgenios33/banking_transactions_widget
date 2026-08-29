from src.data_readers import read_data_from_csv, read_data_from_xlsx
from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import read_data_from_json
from src.widget import get_date, mask_account_card


def main() -> list[dict]:
    """
    Основная точка входа программы для работы с банковскими транзакциями.

    Функция реализует интерактивный цикл обработки данных:
      1. Предлагает пользователю выбрать источник данных (JSON, CSV или XLSX).
      2. Запрашивает и валидирует статус операции для фильтрации (EXECUTED, CANCELED, PENDING).
      3. Позволяет отсортировать операции по дате (по возрастанию или убыванию).
      4. Даёт возможность отфильтровать транзакции только по валюте RUB.
      5. Поддерживает текстовый поиск по полю 'description'.
      6. Выводит итоговый список отфильтрованных и отсортированных операций,
         включая дату, описание, замаскированные реквизиты счетов/карт и сумму.

    Возвращает список словарей с транзакциями, прошедшими все этапы фильтрации и сортировки.
    Если подходящих операций нет — возвращает пустой список.
    """
    print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.\n")

    print("""Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")

    while True:
        menu_selection = input().strip()
        if menu_selection in {"1", "2", "3"}:
            break
        print('Некорректный ввод! Введите "1", "2" или "3".')

    if menu_selection == "1":
        file_path, file_type, reader = "./data/operations.json", "JSON-файл", read_data_from_json

    elif menu_selection == "2":
        file_path, file_type, reader = "./data/transactions.csv", "CSV-файл", read_data_from_csv

    else:
        file_path, file_type, reader = "./data/transactions_excel.xlsx", "XLSX-файл", read_data_from_xlsx

    operations = reader(file_path)
    print(f"\nДля обработки выбран {file_type}.\n")

    print("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    valid_states = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        state_selection = input().upper().strip()
        if state_selection in valid_states:
            break

        print(f'Статус операции "{state_selection}" недоступен.')

    operations = filter_by_state(operations, state_selection)
    print(f'\nОперации отфильтрованы по статусу "{state_selection}"\n')

    while True:
        sorting_by_date = input("Отсортировать операции по дате? Да/Нет\n").lower().strip()
        if sorting_by_date in {"да", "нет"}:
            break
        print('Некорректный ввод. Введите "да" или "нет".\n')

    if sorting_by_date == "да":
        while True:
            sorting_selection = input('\nОтсортировать "по возрастанию" или "по убыванию"?\n').lower().strip()
            if sorting_selection in {"по возрастанию", "по убыванию"}:
                break
            print('Некорректный ввод. Введите "по возрастанию" или "по убыванию".')

        descending = sorting_selection == "по убыванию"
        operations = sort_by_date(operations, descending=descending)

    while True:
        rub_filtered = input("\nВыводить только рублевые транзакции? Да/Нет\n").lower().strip()
        if rub_filtered in {"да", "нет"}:
            break
        print('Некорректный ввод. Введите "да" или "нет".')

    if rub_filtered == "да":
        operations = list(filter_by_currency(operations, "RUB"))

    while True:
        filter_by_word = (
            input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower().strip()
        )
        if filter_by_word in {"да", "нет"}:
            break
        print('Некорректный ввод. Введите "да" или "нет".')

    if filter_by_word == "да":
        while True:
            search_string = input("\nВведите строку или подстроку для поиска.\n").strip()
            if not search_string:
                print("Вы ничего не ввели. Попробуйте снова.")
                continue
            else:
                operations = process_bank_search(operations, search_string)
                break

    if operations:
        print("\nРаспечатываю итоговый список транзакций...\n")

        print(f"Всего банковских операций в выборке: {len(operations)}\n")

        for operation in operations:
            date_str = operation.get("date", "")
            description = operation.get("description", "Описание отсутствует")
            if date_str:
                formatted_date = get_date(date_str)
                print(f"{formatted_date} {description}")
            else:
                print(description)

            from_account_masked = mask_account_card(operation.get("from", ""))
            to_account_masked = mask_account_card(operation.get("to", ""))
            if from_account_masked:
                print(f"{from_account_masked} -> {to_account_masked}")
            else:
                print(to_account_masked)

            amount = operation.get("amount", "0")
            currency_name = operation.get("currency_name", "")
            nested_amount = operation.get("operationAmount", {}).get("amount", "0")
            nested_currency_name = operation.get("operationAmount", {}).get("currency", {}).get("name", "")
            if currency_name:
                print(f"Сумма: {amount} {currency_name}\n")
            elif nested_currency_name:
                print(f"Сумма: {nested_amount} {nested_currency_name}\n")
            else:
                print("Сумма не указана.\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    return operations


if __name__ == "__main__":
    main()
