#!/usr/bin/env python3
'''
Asynchronous coroutine that taks an integer argument,
Waits for ten sec and returns it
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    select rondom figure between 0-max_delay and return it
    '''
    dlay = random.uniform(0, max_delay)
    await asyncio.sleep(dlay)
    return dlay
