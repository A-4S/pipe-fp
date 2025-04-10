from functools import reduce
from typing import Any, Callable, overload

from .type import (
    T0,
    T1,
    T2,
    T3,
    T4,
    T5,
    T6,
    T7,
    T8,
    T9,
)


@overload
def pipe(
    f1: Callable[[T0], T1],
) -> T1: ...


@overload
def pipe(
    f1: Callable[[T0], T1],
    f2: Callable[[T1], T2],
) -> T2: ...


@overload
def pipe(
    f1: Callable[[T0], T1],
    f2: Callable[[T1], T2],
    f3: Callable[[T2], T3],
) -> T3: ...


@overload
def pipe(
    f1: Callable[[T0], T1],
    f2: Callable[[T1], T2],
    f3: Callable[[T2], T3],
    f4: Callable[[T3], T4],
) -> T4: ...


@overload
def pipe(
    f1: Callable[[T0], T1],
    f2: Callable[[T1], T2],
    f3: Callable[[T2], T3],
    f4: Callable[[T3], T4],
    f5: Callable[[T4], T5],
) -> T5: ...


@overload
def pipe(
    f1: Callable[[T0], T1],
    f2: Callable[[T1], T2],
    f3: Callable[[T2], T3],
    f4: Callable[[T3], T4],
    f5: Callable[[T4], T5],
    f6: Callable[[T5], T6],
) -> T6: ...


@overload
def pipe(
    f1: Callable[[T0], T1],
    f2: Callable[[T1], T2],
    f3: Callable[[T2], T3],
    f4: Callable[[T3], T4],
    f5: Callable[[T4], T5],
    f6: Callable[[T5], T6],
    f7: Callable[[T6], T7],
) -> T7: ...


@overload
def pipe(
    f1: Callable[[T0], T1],
    f2: Callable[[T1], T2],
    f3: Callable[[T2], T3],
    f4: Callable[[T3], T4],
    f5: Callable[[T4], T5],
    f6: Callable[[T5], T6],
    f7: Callable[[T6], T7],
    f8: Callable[[T7], T8],
) -> T8: ...


@overload
def pipe(
    f1: Callable[[T0], T1],
    f2: Callable[[T1], T2],
    f3: Callable[[T2], T3],
    f4: Callable[[T3], T4],
    f5: Callable[[T4], T5],
    f6: Callable[[T5], T6],
    f7: Callable[[T6], T7],
    f8: Callable[[T7], T8],
    f9: Callable[[T8], T9],
) -> T9: ...


def pipe(*f: Callable[..., Any]) -> Callable:
    """
    ## Description
    Functionally streamlines a series of function calls.

    ## Example
    .. code-block:: python
        def title_case(msg: str) -> list[str]:
            return pipe(
                str.lower,
                str.title,
                str.split
            )(msg)

    **Returns**
    >>> title_case('WHY, HELLO THERE! 😊')
    ['Why,', 'Hello', 'There!', '😊']
    """

    return lambda x: reduce(lambda a, f: f(a), f, x)
