"""
Tests using pytest-asyncio
They still run sequentially, just like how pytest runs synchronous tests.
Each asynchronous test runs within its assigned event loop.

This sequential execution is intentional and important for maintaining test isolation.
Running tests concurrently could introduce race conditions and side effects where one test could interfere with another,
making test results unreliable and difficult to debug.
"""

import asyncio


async def test_first():
    await asyncio.sleep(2)


async def test_second():
    await asyncio.sleep(2)
