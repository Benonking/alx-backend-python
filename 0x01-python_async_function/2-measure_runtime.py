#!/usr/bin/env python3
'''
Calculate the execution time of a function
'''
from time import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    calculate the averag execution time of a method
    '''
    start = time()

    asyncio.run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
