import time

import redis


class Foo:
    def __init__(self): ...

    def generate_memes(self):
        return 'Super dank meme'

    def slowbro(self):
        time.sleep(5)
        return 'This is an intentionally slow test'

    def herp(self):
        return 'Derp'

    def check_redis(self):
        r = redis.Redis(host='localhost', port=6379)
        return r.info()


def main():
    foo = Foo()
    print(foo.generate_memes())
    print(foo.herp())


