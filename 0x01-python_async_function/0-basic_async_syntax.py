#!/usr/bin/env python3
"""
task-0-basic_async_syntax
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random: asynchronous coroutine that takes in an integer argument
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
