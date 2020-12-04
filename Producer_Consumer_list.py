import sys
import random
import time
from threading import *

lock = Lock()


class Producer(Thread):
    def __init__(self, items, lock):
        Thread.__init__(self)
        self.items = items
        self.producers_lock = Lock()

    def produce_item(self):
        self.items.append(1)
        print("{}: item produit".format(self.name))

    def wait(self):
        attente = 0.2
        attente += random.randint(1, 60) / 100
        time.sleep(attente)

    def run(self):
        while 1:
            self.wait()
            self.producers_lock.acquire()
            self.produce_item()
            self.producers_lock.release()
            self.wait()


class Consumer(Thread):
    def __init__(self, items, lock):
        Thread.__init__(self)
        self.items = items
        self.consumers_lock = Lock()

    def consume_item(self):
        item = self.items.pop()
        print("{}: item consomme".format(self.name))

    def wait(self):
        attente = 0.2
        attente += random.randint(1, 60) / 100
        time.sleep(attente)

    def run(self):
        while 1:
            self.wait()
            self.consumers_lock.acquire()
            self.consume_item()
            self.consumers_lock.release()


if __name__ == "__main__":

    count_producers = 5
    count_consumers = 5
    items = []
    producers = []
    consumers = []

    for i in range(count_producers):
        proc = Producer(items, lock)
        producers.append(proc)
        proc.start()

    for i in range(count_consumers):
        proc = Consumer(items, lock)
        consumers.append(proc)
        proc.start()

    for p in producers:
        p.join()

    for c in consumers:
        c.join()
