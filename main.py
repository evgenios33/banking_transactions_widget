from src.utils import convert_json_file
from src.external_api import convert_transaction_amount


path_to_file = "/Users/evgenios_33/PycharmProjects/banking_transactions_widget/data/operations.json"
if __name__ == "__main__":
    print(convert_json_file(path_to_file))
    print(type(convert_json_file(path_to_file)))


transaction_rub = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}
transaction_usd = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}
transaction_eur = {
    "id": 27192367,
    "state": "CANCELED",
    "date": "2018-12-24T20:16:18.819037",
    "operationAmount": {"amount": "991.49", "currency": {"name": "EURO", "code": "EUR"}},
}


if __name__ == "__main__":
    print(convert_transaction_amount(transaction_rub))
    print(type(convert_transaction_amount(transaction_rub)))
    print(convert_transaction_amount(transaction_usd))
    print(type(convert_transaction_amount(transaction_usd)))
    print(convert_transaction_amount(transaction_eur))
    print(type(convert_transaction_amount(transaction_eur)))
