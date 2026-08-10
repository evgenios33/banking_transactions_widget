import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def convert_transaction_amount(data_dict: dict) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции ("amount") в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли."""
    try:
        currency_code = data_dict.get("operationAmount", {}).get("currency", {}).get("code", "")
        amount = data_dict.get("operationAmount", {}).get("amount", "")

        if not currency_code or not amount:
            raise ValueError("Недостаточно данных в транзакции.")

        amount = float(amount)

        if currency_code != "RUB":

            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"

            payload = {}  # type: ignore
            headers = {"apikey": f"{API_KEY}"}

            try:
                response = requests.request("GET", url, headers=headers, data=payload)
                response.raise_for_status()
                result = response.json()

                if "result" in result:
                    return round(result["result"], 2)  # type: ignore
                else:
                    print("Недостаточно данных в ответе API, возвращаю сумму без конвертации.")
            except requests.RequestException:
                print("Ошибка при выполнении запроса к API. Возвращается исходная сумма.")
        return amount
    except (ValueError, TypeError) as e:
        print(f"Ошибка обработки данных транзакции: {e}. Возвращается 0.0")
        return 0.0
