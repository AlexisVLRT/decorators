import time
from concurrent.futures.thread import ThreadPoolExecutor
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


my_class = MyClass()

# Call do_something_not_thread_safe 5 times at once
with ThreadPoolExecutor() as executor:
    results = list(executor.map(my_class.do_something_not_thread_safe, range(5)))

print(results)
