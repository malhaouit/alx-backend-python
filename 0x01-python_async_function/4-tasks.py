"""This module includes a function that execute multiple coroutines at the
same time"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Creates an async routine.
    Args:
        n (int): Integer number, it represents the number of times we spawn
        `wait_random` routine with the specified `max_delay`.
        max_delay (int): Integer value, a max delay for `wait_random` routine
        to waits.

    Returns:
        List of all the delays in ascending order."""

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = await asyncio.gather(*tasks)
    return sorted(delays)
