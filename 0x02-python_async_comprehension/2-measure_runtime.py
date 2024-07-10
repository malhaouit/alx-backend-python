#!/usr/bin/env python3
"""This module includes a function that measure the runtime"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel using asyncio.gather
    and return total runtime.

    Args:
        None

    Returns:
        Total runtime"""
    start_time = time.time()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()

    return end_time - start_time
