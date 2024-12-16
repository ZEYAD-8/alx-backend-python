#!/usr/bin/env python3
"""
task-1-concurrent_coroutines
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    wait_n: asynchronous coroutine that spawns
    `wait_random_max_delay` n times with
    the specified max_delay.
    Returns a list of floating-point numbers
    representing the delays, sorted in ascending order.

    * to unpack the list of arguments
    asyncio.gather() to run multiple coroutines concurrently
    and collect their results in a list.

    iterates over that sequence. For each iteration,
    the loop runs once. The total number of iterations is n.
    """
    wait_times = await asyncio.gather(
        *(wait_random(max_delay) for _ in range(n)))
    return sorted(wait_times)
