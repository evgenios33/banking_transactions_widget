import pytest


@pytest.fixture
def list_of_dict_for_state() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428835, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 74628835, "state": "INACTIVE", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719456, "state": "ACTIVE", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226111, "state": "INACTIVE", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 354626727, "state": "ACTIVE", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615068573, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 364064591, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dict_for_date() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428835, "state": "EXECUTED", "date": "2020-03-03T18:35:29.512364"},
        {"id": 74628835, "state": "INACTIVE", "date": "2025-07-11T18:35:29.512364"},
        {"id": 939719456, "state": "ACTIVE", "date": "2015-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226111, "state": "INACTIVE", "date": "2022-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-01-15T21:27:25.241689"},
        {"id": 354626727, "state": "ACTIVE", "date": "2025-02-13T21:27:25.241689"},
        {"id": 615068573, "state": "PENDING", "date": "2024-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-10-05T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2026-10-17T08:21:33.419441"},
        {"id": 364064591, "state": "PENDING", "date": "2013-10-25T08:21:33.419441"},
    ]
