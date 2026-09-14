"""
Unit tests should test small, incremental functions for correctness.

They are the least useful in the sense that they are least likely to
be able to tell you if your application as a whole is functioning correctly.

They are good at catching unexpected edge cases, and confirming that a
particular implementation is correct.
"""

import pytest

from your_code_is_trash import foo


@pytest.fixture
def foo_cls():
    return foo.Foo()


def test_foo_can_generate_memes(foo_cls):
    assert foo_cls.generate_memes() == 'Super dank meme'


@pytest.mark.slow
def test_that_foo_is_slow(foo_cls):
    assert foo_cls.slowbro() == 'This is an intentionally slow test'


def test_foo_can_herp(foo_cls):
    assert foo_cls.herp() == 'Derp'
