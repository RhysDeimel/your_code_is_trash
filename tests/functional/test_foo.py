"""
Functional testing should test larger groupings of code.
This should be where a majority of your tests exist.

Preferably, these tests should be approached from an external perspective,
and should use application inputs and outputs, without reaching in to
internal structures or workings (black-box testing).

In doing so, you mimic intended user behavior, and can better assert that
your application functions as intended.
"""

from your_code_is_trash.foo import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Super dank meme\nDerp\n'
