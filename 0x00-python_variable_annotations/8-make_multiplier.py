#!/usr/bin/env python3
''' function make_multiplier that takes a float as argument,
returns a function that multiplies a float by multiplier
'''
from typing import Callable


def make_multiplier(mulitiplier: float) -> Callable[[float], float]:
    '''return a function that multiplies a flaot by multiplirt'''
    def func_mult(n: float) -> float:
        '''muiltpy n by mul;tiplier'''
        return mulitiplier * n
    return func_mult
