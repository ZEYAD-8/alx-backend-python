#!/usr/bin/env python3
""" 101-safely_get_value.py """
from typing import Sequence, Any, Union, Mapping, TypeVar

T = TypeVar("T", bound=Any)


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """safely_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default
