import time
import queue

from functools import partial
from threading import Thread, Timer, Lock


def callback(i):
    print(i)


# t = Timer(10, callback)
# t.start()
# t.join()


class SetInterval(Thread):
    def __init__(self, callback, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lock = Lock()
        self.callback = callback
        self.count = 0

    def run(self):
        while True:
            time.sleep(1)
            callback = partial(self.callback, self.count)
            with self.lock:
                t = Timer(1, callback)
                t.start()
                self.count += 1


t = SetInterval(callback, daemon=True)
t.start()

time.sleep(7)