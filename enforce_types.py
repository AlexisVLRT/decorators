from typeguard import typechecked


@typechecked
def take_a_int(arg: int) -> int:
    return arg


result = take_a_int("Not an int")
print(result)
