from functools import wraps
from time import time
from typing import Any, Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def log(filename: str | None = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
            try:
                start = time()
                result = func(*args, **kwargs)
                end = time()
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(
                            f"Function {func.__name__} OK!\nTime execution: {end - start:.6f}\nResult: {result}\n\n"
                        )
                else:
                    print(f"Function {func.__name__} OK!\nTime execution: {end - start:.6f}\nResult: {result}")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"Function {func.__name__} error: {e}\nInputs: {args}, {kwargs}\n\n")
                else:
                    print(f"Function {func.__name__} error: {e}\nInputs: {args}, {kwargs}")
                return e

        return wrapper

    return decorator
