import sys
import random
import time
from threading import *

lock = Lock()

class Producer(Thread):
    def __init__(self, items):
        Thread.__init__(self)
        self.items = items

    def produce_item(self):
        lock.acquire()
        num = random.randint(1, 100)
        self.items.append(num)
        lock.release()
        print("{}: item produit {}".format(self.name, num))
        print(str(items)+f"<{len(items)}>")

    def wait(self):
        attente = 0.2
        attente += random.randint(1, 60) / 10
        time.sleep(attente)

    def run(self):
        while True:
            self.produce_item()
            self.wait()


class Consumer(Thread):
    def __init__(self, items):
        Thread.__init__(self)
        self.items = items

    def consume_item(self):
        if items:
            lock.acquire()
            item = self.items.pop(0)
            lock.release()
            print("{}: item consomme {}".format(self.name, item))
            print(str(items)+f"<{len(items)}>")


    def wait(self):
        attente = 0.2
        attente += random.randint(1, 60) / 10
        time.sleep(attente)

    def run(self):
        while True:
            self.consume_item()
            self.wait()


if __name__ == "__main__":

    PRODUCERS = 3
    CONSUMERS = 1
    
    items = []
    producers = []
    consumers = []

    for _ in range(PRODUCERS):
        thread = Producer(items)
        consumers.append(thread)
        consumers[-1].start()

    for _ in range(CONSUMERS):
        thread = Consumer(items)
        consumers.append(thread)
        consumers[-1].start()

    for p in producers:
        p.join()

    for c in consumers:
        c.join()
