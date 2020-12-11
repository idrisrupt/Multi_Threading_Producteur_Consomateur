import random
import time
from threading import *
from queue import Queue


class Producer(Thread):
    def __init__(self, ):
        Thread.__init__(self)

    def produce_item(self):
        num = random.randint(1,100)
        items.put(num)
        print("{}:produced {}".format(self.name,num))
        print(str(list(items.queue))+f"<{items.qsize()}>")
        

    def wait(self):
        attente = 0.2
        attente += random.randint(1, 60) / 10
        time.sleep(attente)

    def run(self):
        while 1:
            self.wait()
            self.produce_item()
            


class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def consume_item(self):
        num = items.get()
        print("{}: consumed {}".format(self.name,num))
        print(str(list(items.queue))+f"<{items.qsize()}>")

    def wait(self):
        attente = 0.2
        attente += random.randint(1, 60) / 10
        time.sleep(attente)

    def run(self):
        while 1:
            self.wait()
            self.consume_item()
            


if __name__ == "__main__":

    PRODUCERS = 3
    CONSUMERS = 1

    items = Queue(10)
    producers = []
    consumers = []


    for _ in range(PRODUCERS):
        thread = Producer()
        consumers.append(thread)
        consumers[-1].start()

    for _ in range(CONSUMERS):
        thread = Consumer()
        consumers.append(thread)
        consumers[-1].start()

    for p in producers:
        p.join()

    for c in consumers:
        c.join()