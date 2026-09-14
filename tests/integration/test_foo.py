"""
Functional tests should test your applications' interactions with
external systems.

Because you need to coordinate with other services, these can be the most challenging
and time-consuming tests to write and maintain. However, because you are actually
interacting with other systems (instead of fakes), these tests provide the most realistic
feedback that your application is functioning as intended.
"""

import time
import timeit

import docker
import pytest
import redis

from your_code_is_trash.foo import Foo


@pytest.fixture
def redis_container():
    def wait_until_responsive(check, timeout=30.0, pause=0.1):  # pragma: no cover
        clock = timeit.default_timer
        ref = clock()
        now = ref
        while (now - ref) < timeout:
            if check():
                return
            time.sleep(pause)
            now = clock()

        raise Exception('Timeout reached while waiting on service!')  # noqa: TRY002, TRY003

    def is_responsive():
        try:
            r = redis.Redis(host='localhost', port=6379, db=0)
            r.info()
        except redis.exceptions.ConnectionError:
            return False
        else:
            return True

    client = docker.from_env()
    container = client.containers.run('redis', detach=True, ports={6379: 6379}, remove=True)
    wait_until_responsive(check=lambda: is_responsive())
    yield
    container.kill()


@pytest.mark.slow
def test_foo_can_talk_to_redis(redis_container):
    foo = Foo()
    assert foo.check_redis()
