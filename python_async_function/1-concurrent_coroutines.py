#!/usr/bin/env python3
"""Concurrent coroutines using asyncio module."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay."""
    arr = []
    for i in range(n):
        arr.append(wait_random(max_delay))

    delays = await asyncio.gather(*arr)
    sorted_delays = []
    while delays:
        smallest = min(delays)
        sorted_delays.append(smallest)
        delays.remove(smallest)
    return sorted_delays
