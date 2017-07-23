class Foo:
    pass


class Fib:
    pass


class Employee(Foo):
    #__slots__ = ['previous', 'current']

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{0}.{1}@gmail.com".format(self.first, self.last)

    @email.setter
    def email(self, address):
        self.emailaddress = address

    @email.deleter
    def email(self):
        del self.emailaddress

    def next(self):
        self.previous, self.current = self.current, self.previous + self.current
        return self.previous

a = Employee("John", "Smith")
print(a.email)
a.email = "a.ddddd@gmail.com"
print(a.emailaddress)
print(a.__dict__)
del a.email
print(a.__dict__)

print(issubclass(Employee, Fib))

"""print(a.previous, a.current)
a.current += 6
print(a.current)"""


def fibGenerator(numTerms):
    first = 0
    second = 1
    for i in range(numTerms):
        yield first
        first, second = second, first + second


def fibrecurse(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibrecurse(n - 1) + fibrecurse(n - 2)


def squares(x):
    result = []
    for i in x:
        return result.append(i)


"""fibs = Fib()
for i in fibs:
    if i < 50:
        print i
    else:
        break"""


def foo(a, b, c):
    print(locals())
    return ','.join(v for v in locals().values() if v is not None)

# print(foo('Cleese', 'Palin', 'None'))


"""def nones(a, b, c, d):
    arguments = locals()
    print 'The following arguments are not None: ', ', '.join(k for k, v in arguments.items() if v is not None)"""

# nones("Something", None, 'N', False)
