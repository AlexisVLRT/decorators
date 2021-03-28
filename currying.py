from toolz import curry


@curry
def add(a, b):
    return a + b


add_partial = add(1)
add_final = add_partial(2)

print(add_partial)
print(add_final)
