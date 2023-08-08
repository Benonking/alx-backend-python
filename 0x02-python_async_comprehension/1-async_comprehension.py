#!/usr/bin/env python3
'''
Generate async comprehension from generator object
'''
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    '''get Genrotor object and return it'''
    return [i async for i in async_generator()]
