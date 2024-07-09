#!/usr/bin/envpython3
"""This module contains a async_generator() function that creates asynchronous
generator."""

from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """Creates a coroutine that loops 10 times, each time asynchronously wait
    1 second, then yield a random number between 0 and 10.

    Args: (No arguments).

    Returns:
    A synchronous generator yielding floats."""

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
