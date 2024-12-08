#!/usr/bin/env python3
"""Asyncoroutine module"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """Returns a list of delays in ascending order."""
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    delays = await asyncio.gather(*tasks)

    sorted_delays = []
    while delays:
        smallest = min(delays)
        sorted_delays.append(smallest)
        delays.remove(smallest)

    return sorted_delays
