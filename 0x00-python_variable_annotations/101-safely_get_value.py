#!/usr/bin/env python3
''' safely get value from dictionary'''
from typing import Dict, Mapping, Any, Union, Optional, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    '''
    Safely gt value from dictionary with TypeVar
    Args:
      dict: Dictionary to get value from
      key: Key to get value from
      default: default value if not found
    Returns:
      value
    '''
    if key in dict:
        return dct[key]
    else:
        return default
