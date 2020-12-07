from threading import Thread
import time
import random
from queue import Queue

queue = Queue(10)


class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print("Produced", num)
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print("Consumed", num)
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()

# from threading import RLock, Thread
# import time
# import random


# verrou = RLock()
# queue = []


# class ConsumerThread(Thread):
#     def run(self):
#         global queue
#         while True:
#             verrou.acquire()
#             if not queue:
#                 print("Nothing in queue, consumer is waiting")
#                 verrou.wait()
#                 print("Producer added something to queue and notified the consumer")
#             num = queue.pop(0)
#             print("Consumed", num)
#             verrou.release()
#             time.sleep(random.random())


# class ProducerThread(Thread):
#     def run(self):
#         nums = range(5)
#         global queue
#         while True:
#             verrou.acquire()
#             num = random.choice(nums)
#             queue.append(num)
#             print("Produced", num)
#             verrou.release()
#             time.sleep(random.random())


# ProducerThread().start()
# ConsumerThread().start()
