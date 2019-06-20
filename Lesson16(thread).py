import time
from threading import Thread, Lock  #потоки threading продовжують працювати при закритті основного потоку

count = 0

lock = Lock()

def worker():
    global count
    for _ in range(5):
        with lock:
            count +=1
            time.sleep(.005)
            print(count)
            count +=1

threads = []

for i in range(10):
    thread = Thread(name=f'(i)', target=worker, args=())
    thread.daemon = True    #параметр завершує дочірні потоки при закритті основного
    threads.append(thread)      #ініціалізуємо потоки

for thread in threads:
    thread.start()      #запускаємо потоки

for thread in threads:
    thread.join()       #join очікує закінчення виконання дочірніх потоків

print('count = ',count)