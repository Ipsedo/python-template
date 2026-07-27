from typing import TypeVar

T = TypeVar("T")


def identity(variable: T) -> T:
    return variable
