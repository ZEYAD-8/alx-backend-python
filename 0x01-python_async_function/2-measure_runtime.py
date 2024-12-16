#!/usr/bin/env python3
"""
task-2-measure_runtime
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time: measure the total execution time for
    wait_n(n, max_delay), and return average execuation time
    per operation (n).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
