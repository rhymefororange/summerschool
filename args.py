def simplefunc(x, y):
    return x * y


def defaultargfunc(x, y, z=[6]):
    z.append(x * y)
    return z


def varargfunc(x, y, *args):
    print(x)
    print(y)
    print(args)
    result = x + y
    for arg in args:
        result += arg
    return result


def varkwargfunc(x, y, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)
    result = x + y
    for key in kwargs.values():
        result += key
    return result


if __name__ == '__main__':
    print(varkwargfunc(1, 2, 6, 7, 89, z=3, p=4))
