x = 6


def example():
    print(x)
    # z, however, is a local variable.
    z = 5
    # this works
    print(z)


def example2():
    print(x)
    print(x + 5)
    x += 6
    print(x)


def example3():
    global x
    # now we can:
    print(x)
    x += 5
    print(x)


def example4():
    globx = x
    # now we can:
    print(globx)
    globx += 5
    print(globx)


def example5(modify):

    print(modify)
    modify += 5
    print(modify)
    return modify


if __name__ == "__main__":
    example2()
    print(x)
    # print(z)

    #y = example5(x)
    # print(x)
    # print(y)
