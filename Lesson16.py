import _thread
import time

print(dir(_thread))

lock = _thread.allocate()


def worker(id):
                                    #lock.acquire()
    with lock:
        time.sleep(2)
        print(_thread.get_ident())
                                    #lock.release()

for i in range(5):
    _thread.start_new_thread(worker, (i,))

time.sleep(10)