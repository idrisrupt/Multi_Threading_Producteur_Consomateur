import sys
import random
import time
from threading import *


class Producer(Thread):
    def __init__(self, items):
        Thread.__init__(self)
        self.items = items

    def produce_item(self):
        num = random.randint(1, 100)
        self.items.append(num)
        print("{}: item produit {}".format(self.name, num))

    def wait(self):
        attente = 0.2
        attente += random.randint(1, 60) / 100
        time.sleep(attente)

    def run(self):
        while 1:
            self.wait()
            self.produce_item()
            self.wait()


class Consumer(Thread):
    def __init__(self, items):
        Thread.__init__(self)
        self.items = items

    def consume_item(self):
        item = self.items.pop(0)
        print("{}: item consomme {}".format(self.name, item))

    def wait(self):
        attente = 0.2
        attente += random.randint(1, 60) / 100
        time.sleep(attente)

    def run(self):

        while 1:
            self.wait()
            self.consume_item()
            self.wait()


if __name__ == "__main__":

    count_producers = 2
    count_consumers = 3
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
