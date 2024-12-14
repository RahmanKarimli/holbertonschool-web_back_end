#!/usr/bin/env python3
"""
Async Comprehension
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """async comprehension"""
    start_time: float = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time: float = time.time()
    return end_time - start_time
