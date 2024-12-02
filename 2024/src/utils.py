from typing import Callable, Iterable


def count_if(iterable: Iterable, callable: Callable) -> int:
    return sum(1 for item in iterable if callable(item))