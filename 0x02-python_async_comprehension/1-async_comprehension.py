#!/usr/bin/env python3
"""This module includes a function that creates a coroutine called
`async_comprehension`"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Creates a coroutine that collects 10 random numbers from
    async_generator() and return them.

    Args:
        None

    Returns:
        10 random numbers"""

    return [number async for number in async_generator()]
