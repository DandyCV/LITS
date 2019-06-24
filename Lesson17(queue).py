import time
import queue

from threading import Thread, Lock
from multiprocessing import Process, Queue, Pipe      #об'єкт процесу та черга процесів. Pipe - двухстороння черга


q = queue.Queue(5)  # об'єкт черги
lock = Lock()


def write_worker(q):
    for i in range(10):
        try:
            time.sleep(1)
            q.put(i)
           # q.put(i, block=True, timeout=1)    # відправляємо в чергу: і - повідомлення,
                                                # block - чи очікувати при переповненні черги чи піднімати помилку
                                                # timeout - скільки очікувати пере підняттям помилки
        except queue.Full:
            return


def read_worker(q):
    while True:
        try:
            time.sleep(0.5)
            #item = q.get_nowait()
            item = q.get(timeout=0.5)           # забираємо з черги: і - повідомлення,
                                                # block - чи очікувати при пустаті в черзі чи піднімати помилку
                                                # timeout - скільки очікувати пере підняттям помилки
            print(item)
        except queue.Empty:
            return

w = Thread(target=write_worker, args=(q,))
r = Thread(target=read_worker, args=(q,))

w.start()
r.start()

w.join()
r.join()
