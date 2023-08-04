#!/usr/bin/env python3
'''Augmented code with duck typed annotations'''
from typing import List, Iterable, Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''return first elemet of None'''
    if lst:
        return lst[0]
    else:
        return None
