#!/usr/bin/env python3
"""
task-4-tasks
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute task_wait_random n times
    """
    wait_times = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n)))
    return sorted(wait_times)
