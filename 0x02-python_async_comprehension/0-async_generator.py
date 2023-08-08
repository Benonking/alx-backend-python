#!/usr/bin/env python3
'''
Coroutine loops ten times and yeads random number
'''
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Loop couritne ten times and sleep
    for one second after every loop
    '''
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield genRandom()


def genRandom() -> float:
    rand = random.uniform(0, 10)
    return rand
