#!/usr/bin/env python3
'''
Calculate Run time of four
'''
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measure run time of a funtion
    '''
    start = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time()
    return end - start
