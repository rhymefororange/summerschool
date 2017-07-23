# acc is mutable and stays the same for all future
# function calls if it wasn't called with explicitly
# passing acc, for example: badunique([1,2], acc=[])


def badunique(iterable, acc=[]):
    for item in iterable:
        acc.append(item)
    return acc


# Now it remembers the seen items between
# different function calls if seen is not passed
# explicitly.
# If this is not desirable, go to the third example
def unique_with_seen(iterable, seen=set()):
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    print(seen)
    return acc


# Here the function behaves correctly
# for each input independently of the
# previous inputs
def unique(iterable, acc=None):
    if acc is None:
        acc = []
    for item in iterable:
        acc.append(item)
    return acc

xs = [1, 2, 4, 5, 66, 66, 66, 5, 4, 4, 4, 1]
s = [8, 8, 8, 0, 1, 2, 3]
print(unique(xs))
print(unique(xs))
print(unique(s))
