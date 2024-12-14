#!/usr/bin/env python3
'''
Module defines a coroutine called async_comprehension
that takes no arguments.
'''
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Function for async comprehension
    '''
    result = [num async for num in async_generator()]
    return result
