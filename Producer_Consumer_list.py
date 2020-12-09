import sys
import random
import time
from threading import *


lock = Lock()


class Producer(Thread):
    def __init__(self, items):
        Thread.__init__(self)
        self.items = items
        # self.producers_lock = RLock()

    def produce_item(self):
        global items
        num = random.randint(1, 100)
        self.items.append(num)
        print("{}: item produit {}".format(self.name, num))

    def wait(self):
        attente = 0.2
        attente += random.randint(1, 60) / 100
        time.sleep(attente)

    def run(self):
        try:
            while 1:
                self.wait()

                # self.producers_lock.acquire()
                self.produce_item()
                # self.producers_lock.release()
                self.wait()
        finally:
            lock.release()


class Consumer(Thread):
    def __init__(self, items):
        Thread.__init__(self)
        self.items = items

    def consume_item(self):
        global items
        item = self.items.pop(0)
        print("{}: item consomme {}".format(self.name, item))

    def wait(self):
        attente = 0.2
        attente += random.randint(1, 60) / 100
        time.sleep(attente)

    def run(self):
        lock.acquire()
        try:
            while 1:
                self.wait()

                self.consume_item()

        finally:
            lock.release()


if __name__ == "__main__":

    lock = Lock()

    count_producers = 5
    count_consumers = 5
    items = []
    producers = []
    consumers = []

    for i in range(count_producers):
        proc = Producer(items)
        producers.append(proc)
        proc.start()

    for i in range(count_consumers):
        proc = Consumer(items)

        consumers.append(proc)
        proc.start()

    for p in producers:
        p.join()

    for c in consumers:
        c.join()
