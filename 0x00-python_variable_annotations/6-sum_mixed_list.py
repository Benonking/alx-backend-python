#!/usr/bin/env python3
'''function takes a list of loats and ints and returns the sum'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''retun sum'''
    return sum(mxd_lst)
