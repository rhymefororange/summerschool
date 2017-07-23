x = 'global x'


def outer():
    #x = 'outer x'
    # for b in range(3):
    #    x = 'outer {}'.format(b)

    def inner():
        #x = 'inner x'

        # for c in range(4):
        #    x = 'inner {}'.format(c)
        print(x)

    inner()
    print(x)


outer()
print(x)
