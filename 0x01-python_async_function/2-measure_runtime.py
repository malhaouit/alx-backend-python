#!/usr/bin/env python3
"""This module includes a function that measure the runtime."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for `wait_n(n, max_delay)`.

    Args:
        n (int): Integer, number of the spawned `wait_random` function.
        max_delay: Integer number, a max delay for `wait_random`.

    Returns:
        Total time divided by n (total_time / n)"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
