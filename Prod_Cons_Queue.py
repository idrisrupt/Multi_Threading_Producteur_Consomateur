import random
import time
from threading import *
from queue import Queue


class Producer(Thread):
    def __init__(self, items):
        Thread.__init__(self)
        self.items = items

    def produce_item(self):
        global items
        num = random.randint(1,100)
        items.put(num)
        print("{}:produced an item {}".format(self.name,num))

    def wait(self):
        attente = 0.2
        attente += random.randint(1, 60) / 100
        time.sleep(attente)

    def run(self):
        i = 1
        while i < 3:
            self.wait()
            self.produce_item()
            i += 1
            


class Consumer(Thread):
    def __init__(self, items):
        Thread.__init__(self)
        self.items = items

    def consume_item(self):
        global items
        num = items.get()
        print("{}: consumed an item {}".format(self.name,num))

    def wait(self):
        attente = 0.2
        attente += random.randint(1, 60) / 100
        time.sleep(attente)

    def run(self):
        i = 1
        while i < 3:
            self.wait()
            self.consume_item()
            i += 1
            


if __name__ == "__main__":

    PRODUCERS = 3
    CONSUMERS = 3

    items = Queue(10)
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