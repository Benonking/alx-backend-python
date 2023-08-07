#!/usr/bin/env python3
'''
Run Multiple cocurents all at once
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Return list of delays in ascending order(order of complition)
    Args:
        n: number of times of calling the imported funtion
        max_delay: arg of imported function wait_random
    '''
    res, delays = [], []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))
    # get awaitables in order of completion
    for delay in asyncio.as_completed(delays):
        result = await delay
        res.append(result)
    return res
