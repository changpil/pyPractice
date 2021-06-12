import queue, threading , time
import logging
import random
FORMAT = "[%(threadName)s:%(asctime)s:%(levelname)s] %(message)s"
logging.basicConfig(filename='example.log', level=logging.DEBUG, format=FORMAT)

def producer(queue):
    #while True:
    for _ in range(10):
        item = random.randint(0, 10000)
        logging.info(f"producer: {item}")
        queue.put(item)
        time.sleep(0.5)

def producerFromInput(queue):
    #while True:
    while True:
        item = input("Enter int (0 for exit):")
        item = int(item)
        logging.info(f"producer: {item}")
        queue.put(item)
        time.sleep(0.1)
        if item == 0:
            break

def consumer(queue):
    while True:
        # Wait until queue is filled
        # item = queue.get()
        try:
            # If queue is empty, throw exception
            item = queue.get(block=False)
            queue.task_done()
            logging.info(f"consumer: {item}")
        except :
            logging.info("Queue is empty")
            time.sleep(1)


        if item == 0:
            break

queue = queue.Queue()
t1 = threading.Thread(name="producer", target=producer, args=(queue,))
t2 = threading.Thread(name="consumer", target=consumer, args=(queue,))
t3 = threading.Thread(name="producerFromInput", target=producerFromInput, args=(queue,))
t1.start()
t2.start()
t3.start()


