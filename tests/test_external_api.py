from unittest.mock import Mock, patch

import requests

from src.external_api import convert_transaction_amount


def test_missing_data() -> None:
    data = {"operationAmount": {}}  # type: ignore
    result = convert_transaction_amount(data)
    # Ожидается 0.0 при ошибке обработки
    assert result == 0.0


@patch("src.external_api.requests.request")
def test_already_rub_no_api_call(mock_request: Mock) -> None:
    data = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}

    result = convert_transaction_amount(data)
    # API не вызывается, сумма возвращается как есть
    assert result == 100.0
    mock_request.assert_not_called()


@patch("src.external_api.requests.request")
def test_convert_usd_success(mock_request: Mock) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {"result": 800.0}
    mock_response.raise_for_status = lambda: None
    mock_request.return_value = mock_response

    data = {"operationAmount": {"amount": "10", "currency": {"code": "USD"}}}

    result = convert_transaction_amount(data)
    assert result == 800.0
    mock_request.assert_called_once()


@patch("src.external_api.requests.request")
def test_convert_eur_success(mock_request: Mock) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {"result": 950.0}
    mock_response.raise_for_status = lambda: None
    mock_request.return_value = mock_response

    data = {"operationAmount": {"amount": "10", "currency": {"code": "EUR"}}}

    result = convert_transaction_amount(data)
    assert result == 950.0
    mock_request.assert_called_once()


@patch("src.external_api.requests.request")
def test_api_request_exception(mock_request: Mock) -> None:
    mock_request.side_effect = requests.RequestException()

    data = {"operationAmount": {"amount": "15", "currency": {"code": "USD"}}}

    result = convert_transaction_amount(data)
    # Ожидается возврат исходной суммы (15)
    assert result == 15.0
    mock_request.assert_called_once()
