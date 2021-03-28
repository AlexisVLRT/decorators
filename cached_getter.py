import time

from cached_property import cached_property


class MyClass:
    def __init__(self):
        self._property = "The property value"

    @cached_property
    def a_long_property_to_compute(self):
        time.sleep(5)
        return self._property


my_class = MyClass()

start_time = time.time()
my_class.a_long_property_to_compute
print(f"First call took {round(time.time() - start_time)} seconds")

start_time = time.time()
my_class.a_long_property_to_compute
print(f"Second call took {round(time.time() - start_time)} seconds")
