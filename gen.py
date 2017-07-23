def simple_gen():
    yield 'Oh'
    yield 'hello'
    yield 'there'


class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


def yrangefunc(n):
    i = 0
    while i < n:
        yield i
        i += 1


def squares(integers):
    for i in integers:
        yield i * i


class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def next(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


for i in Fib(10):
    print i


def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
