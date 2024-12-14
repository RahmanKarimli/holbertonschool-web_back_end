#!/usr/bin/env python3
"""Module for asynchronous generator."""
import asyncio
from random import uniform
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Function for asynchronous generator."""
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
