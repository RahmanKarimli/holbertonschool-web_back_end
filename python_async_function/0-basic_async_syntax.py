#!/usr/bin/env python3
"""Basic async syntax."""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random amount of seconds."""
    number = uniform(0, max_delay)
    await asyncio.sleep(number)
    return number
