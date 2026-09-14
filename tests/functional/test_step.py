import pytest


@pytest.mark.incremental
class TestUserHandling:
    def test_login(self):
        pass

    def test_modification(self):
        # change to `False` to see pytest incremental behaviour
        assert True

    def test_deletion(self):
        # This will not run if `test_modification` fails
        pass


def test_normal():
    # This will run if `test_modification` fails because
    #  it has not been marked as incremental
    pass
