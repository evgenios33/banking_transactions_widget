from src.decorators import log


@log()
def my_function(x: int | float, y: int | float) -> int | float:
    """Функция складывающая два числа."""
    return x + y


print(my_function(1, 2))
