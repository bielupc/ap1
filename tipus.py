from typing import Any, TypeAlias, Optional, TypeVar, Union

T = TypeVar("T")

Temepratura: TypeAlias = list[float]

def f(x: Any) -> Any:
    return x

def g(x) -> Optional[int]:
    return x

def h(x: T) -> T:
    return x

def d(x): -> Union[int, str]:
    return x

def s(x: temperatures) -> None:
    return x



