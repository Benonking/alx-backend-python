#!/usr/bin/env python3
'''
Coroutine loops ten times and yeads random number
'''
import random
import asyncio


async def async_generator():
    '''
    Loop couritne ten times and sleep 
    for one second after every loop
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield genRandom()


def genRandom() -> int:
    rand = random.uniform(0, 10)
    return rand
