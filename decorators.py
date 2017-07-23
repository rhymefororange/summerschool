from functools import wraps


def my_decorator(some_function):
    print("Something is happening before wrapper.")

    @wraps(some_function)
    def wrapper(n):
        #print(some_function.__name__, some_function.__doc__,
        #      some_function.__module__)
        print("Something is happening before some_function() is called.")
        print(n)
        some_function(n)

        print("Something is happening after some_function() is called.")

    return wrapper


def once(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            func(*args, **kwargs)
            inner.called = True
    inner.called = False
    return inner


@my_decorator
def just_some_function(n):
    """My documentation

    Detailed description here"""
    for i in range(10):
        yield "Wheee!" + str(n)


# just_some_function = my_decorator(just_some_function, '5')

just_some_function(5)
just_some_function(10)
just_some_function(100)
