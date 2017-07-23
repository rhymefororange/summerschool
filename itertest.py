class fib():
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.curr, self.prev = self.curr + self.prev, self.curr
        return self.prev

    def next(self):
        self.curr, self.prev = self.curr + self.prev, self.curr
        return self.prev


def fibfunc():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


f = fib()
# print(list(islice(f,0,10)))
for i in range(10):
    print(next(f))

"""====================================================="""
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

# prints 4
print(next(my_iter))

# prints 7
print(next(my_iter))

# next(obj) is same as obj.__next__()

# prints 0
print(my_iter.__next__())

# prints 3
print(my_iter.__next__())

# This will raise error, no items left
next(my_iter)
