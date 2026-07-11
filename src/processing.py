def filter_by_state(list_of_dict: list, state_value: str = "EXECUTED") -> list:
    """Возвращает новый список словарей, содержащий только те словари,
    у которых ключ "state" соответствует переданному значению."""
    filter_list = []
    for dict_ in list_of_dict:
        for value in dict_.values():
            if value == state_value.upper():
                filter_list.append(dict_)

    return filter_list


def sort_by_date(list_of_dict: list, sorting_direction: str = "True") -> list:
    """Возвращает новый список отсортированный по ключу "date"."""
    if sorting_direction.title() == "True":
        sorted_list = sorted(list_of_dict, key=lambda x: x["date"], reverse=True)
    else:
        sorted_list = sorted(list_of_dict, key=lambda x: x["date"])

    return sorted_list
