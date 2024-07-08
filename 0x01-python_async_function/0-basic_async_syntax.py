#!/usr/bin/env python3
"""This module includes a function that creates asynchronous coroutine"""

import random
import asyncio


async def wait_random(max_delay=10):
    """This function creates an asynchronous coroutine that takes in an integer
    argument `max_delay` and waits for a random delay between 0 and `max_delay`
    seconds and eventually returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
