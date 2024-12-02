import threading
import time
from functools import reduce

class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=()):
        self.target = target
        self.args = args
        self.result = None
        super().__init__()

    def run(self):
        self.result = self.target(*self.args)

    def join(self, *args):
        super().join(*args)
        return self.result

def secti(num):
    time.sleep(5)
    return reduce(lambda x, y: x + y, range(1, num+1))

def vynasob(num):
    time.sleep(5)
    return reduce(lambda x, y: x * y, range(1, num+1))

thread_secti = ThreadWithReturnValue(target=secti, args=(1000,))
thread_vynasob = ThreadWithReturnValue(target=vynasob, args=(100,))

thread_secti.start()
thread_vynasob.start()

vysledek_secti = thread_secti.join()
vysledek_vynasob = thread_vynasob.join()

print(f"Vysledek scitani cisel od 1 do 1 000 000 je {vysledek_secti}.")
print(f"Vysledek nasobeni cisel od 1 do 100 je {vysledek_vynasob}.")

