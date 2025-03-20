from functools import reduce
from typing import Callable

def pipe(*f: list[Callable]) -> Callable:
    return lambda x: reduce(lambda a, f: f(a), f, x)
