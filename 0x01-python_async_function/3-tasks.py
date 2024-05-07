#!/usr/bin/env python3
"""
Write a function (do not create an async function, use the regular function
syntax to do this) task_wait_random that takes an integer max_delay and
returns a asyncio.Task.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


# def task_wait_random(max_delay: int):
#     """
#         this returns a asyncio.Task
#     """
#     return (asyncio.create_task(wait_random(max_delay)))

def task_wait_random(max_delay):
    async def wrapper():
        return await wait_random(max_delay)

    return asyncio.ensure_future(wrapper())
