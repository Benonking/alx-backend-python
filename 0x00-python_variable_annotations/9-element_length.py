#!/usr/bin/env python3
'''
Function with paramenters (anotations)
 return: Va;lues of appropriate types
'''
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return appropriate types'''
    return [(i, len(1)) for i in lst]
