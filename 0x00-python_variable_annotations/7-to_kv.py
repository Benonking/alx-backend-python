#!/usr/bin/env python3
'''function takes astring and an int and returns a tuple'''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Return a tuble with a k/v pair'''
    return k, v**2
