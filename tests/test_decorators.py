import pytest

from src.decorators import my_function


def test_log(capsys: pytest.CaptureFixture[str], fixed_time: pytest.FixtureDef[float]) -> None:
    my_function(1, 2)
    captured = capsys.readouterr()
    assert "Function my_function OK!" in captured.out
    assert "Result: 3" in captured.out


def test_log_error(capsys: pytest.CaptureFixture[str]) -> None:
    my_function("1", 2)  # type: ignore
    captured = capsys.readouterr()
    assert 'Function my_function error: can only concatenate str (not "int") to str' in captured.out
    assert "Inputs: ('1', 2), {}" in captured.out


def test_log_error_arg(capsys: pytest.CaptureFixture[str]) -> None:
    my_function(1)  # type: ignore
    captured = capsys.readouterr()
    assert "Function my_function error: my_function() missing 1 required positional argument: 'y'" in captured.out
    assert "Inputs: (1,), {}" in captured.out
