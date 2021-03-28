Decorators
==============================

5 novelty python decorators I'll probably forget to use.
------------

Cached property
------------

```python
import time

from cached_property import cached_property


class MyClass:
    def __init__(self):
        self._property = "The property value"

    @cached_property
    def a_long_property_to_compute(self):
        time.sleep(5)
        return self._property
```

<details><summary>Usage</summary>
<p>

With decorator:

```python
my_class = MyClass()

start_time = time.time()
my_class.a_long_property_to_compute
print(f"First call took {round(time.time() - start_time)} seconds")
# First call took 5 seconds

start_time = time.time()
my_class.a_long_property_to_compute
print(f"Second call took {round(time.time() - start_time)} seconds")
# Second call took 0 seconds
```

Without decorator:

```python
my_class = MyClass()

start_time = time.time()
my_class.a_long_property_to_compute
print(f"First call took {round(time.time() - start_time)} seconds")
# First call took 5 seconds

start_time = time.time()
my_class.a_long_property_to_compute
print(f"Second call took {round(time.time() - start_time)} seconds")
# Second call took 5 seconds
```
</p>
</details>

Thread lock
------------
```python
import time
from threading import Lock

from fasteners import locked


class MyClass:
    def __init__(self):
        self._lock = Lock()
        self.construction_time = time.time()

    @locked()
    def do_something_not_thread_safe(self, i):
        time.sleep(1)
        return f"Result {i} obtained after {round(time.time() - self.construction_time)} seconds"
```

<details><summary>Usage</summary>
<p>

With decorator:

```python
from concurrent.futures.thread import ThreadPoolExecutor

my_class = MyClass()

# Call do_something_not_thread_safe 5 times at once
with ThreadPoolExecutor() as executor:
    results = list(executor.map(my_class.do_something_not_thread_safe, range(5)))

print(results)
# ['Result 0 obtained after 1 seconds', 'Result 1 obtained after 2 seconds', 'Result 2 obtained after 3 seconds', 'Result 3 obtained after 4 seconds', 'Result 4 obtained after 5 seconds']
```

Without decorator:

```python
from concurrent.futures.thread import ThreadPoolExecutor

my_class = MyClass()

# Call do_something_not_thread_safe 5 times at once
with ThreadPoolExecutor() as executor:
    results = list(executor.map(my_class.do_something_not_thread_safe, range(5)))

print(results)
# ['Result 0 obtained after 1 seconds', 'Result 1 obtained after 1 seconds', 'Result 2 obtained after 1 seconds', 'Result 3 obtained after 1 seconds', 'Result 4 obtained after 1 seconds']
```

</p>
</details>

Type enforcer
------------
```python
from typeguard import typechecked


@typechecked
def take_a_int(arg: int) -> int:
    return arg
```

<details><summary>Usage</summary>
<p>

With decorator:

```python
result = take_a_int("Not an int")
print(result)
# TypeError: type of argument "arg" must be int; got str instead
```

Without decorator:

```python
result = take_a_int("Not an int")
print(result)
# Not an int
```

</p>
</details>

Singleton
------------
```python
from singleton_decorator import singleton


@singleton
class MyClass:
    pass
```

<details><summary>Usage</summary>
<p>

With decorator:

```python
instance_1 = MyClass()
instance_2 = MyClass()

print(f"Is is {instance_1 is instance_2} that instance_1 is instance_2")
# Is is True that instance_1 is instance_2
```

Without decorator:

```python
instance_1 = MyClass()
instance_2 = MyClass()

print(f"Is is {instance_1 is instance_2} that instance_1 is instance_2")
# Is is False that instance_1 is instance_2
```

</p>
</details>

Currying
------------
```python
from toolz import curry


@curry
def add(a, b):
    return a + b
```

<details><summary>Usage</summary>
<p>

With decorator:

```python
add_partial = add(1)
add_final = add_partial(2)

print(add_partial)
# <function add at 0x7fec081e0a70>
print(add_final)
# 3
```

Without decorator:

```python
add_partial = add(1)
# TypeError: add() missing 1 required positional argument: 'b'
```

</p>
</details>
