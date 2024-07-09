#!/usr/bin/env python3
"""This module contains a async_generator() function that creates an
asynchronous generator"""

from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """Creates a coroutine that loops 10 times, each time asynchronously
    waiting 1 second, then yield a random number between 0 and 10.

    Args:
        None

    Returns:
        AsyncGenerator[float, None]: An asynchronous generator yielding floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
