#!/usr/bin/env python3
"""
    a measure_time function with integers n and max_delay as arguments that
    measures the total execution time for wait_n(n, max_delay), and returns
    total_time / n.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """The average runtime of wait_n
    """
    strt_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - strt_time) / n