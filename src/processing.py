from datetime import datetime


def filter_by_state(list_of_dict: list[dict], state_value: str = "EXECUTED") -> list[dict]:
    """Возвращает новый список словарей, содержащий только те словари,
    у которых ключ "state" соответствует переданному значению."""
    if not list_of_dict or not all("state" in dict_data for dict_data in list_of_dict):
        raise ValueError("Некорректный ввод. Ключ 'state' не найден или значение отсутствует.")

    filter_list = []
    for dict_data in list_of_dict:
        for value in dict_data.values():
            if value == state_value.upper():
                filter_list.append(dict_data)

    return filter_list


def sort_by_date(list_of_dict: list[dict], decrease: bool = True) -> list[dict]:
    """Возвращает новый список отсортированный по ключу "date"."""
    for dict_data in list_of_dict:
        if "date" not in dict_data:
            raise KeyError(f"Ключ 'date' отсутствует в словаре: {dict_data}.")
        try:
            datetime.strptime(dict_data["date"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            raise ValueError(f"Некорректный формат даты в словаре: {dict_data}")

    if decrease:
        sorted_list = sorted(list_of_dict, key=lambda x: x["date"], reverse=True)
    else:
        sorted_list = sorted(list_of_dict, key=lambda x: x["date"])

    return sorted_list
