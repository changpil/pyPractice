import queue, time
from threading import Thread


# def threaded_function(arg):
#   time.sleep(5)
#   arg.put(20)
#
#
# q = queue.Queue()
#
# q.put(3)
# q.put(4)
# print(q.get())
# print(q.get())

# thread = Thread(target = threaded_function, args = (q, ))
# thread.start()
# thread.join()
# print(q.get())

##################################################################
# q = queue.Queue()
#
# q.put(3)
# q.put(4)
# print("size: ", q.qsize())
# print(q.get())
# print(q.get())
# try:
#     print(q.get(False))
# except:
#     pass
# print("size: ", q.qsize())
##################################################################
# from queue import PriorityQueue
# q = PriorityQueue(3)
# q.put(3)
# q.put(4)
# q.put(7)
# import traceback, sys
# try:
#     q.put(8, False)
# except queue.Full as e:
#     exc_type, exc_value, exc_tb = sys.exc_info()
#     print(exc_type)
#     print(exc_value)
#     print(exc_tb)
#     #traceback.print_exception(exc_type, exc_value, exc_tb)
#     #traceback.print_exc(limit=2, file=sys.stdout)
#     print(repr(traceback.format_exception(exc_type, exc_value,
#                                          exc_tb)))
# print(q.get())
# print(q.get())
# print(q.get())
# try:
#     print(q.get(False))
# except queue.Empty:
#     print(queue.Empty)
##################################################################
# import heapq
# li=[5,7,9,1,3, 6]
# heapq.heapify(li)
# print(li)
# li.append(50)
# li.append(2)
# print(li)
#
# heapq.heapify(li)
# print(li)
# heapq.heappush(li,40)
# heapq.heappush(li,7)
# heapq.heappush(li,14)
# heapq.heappush(li,17)
# print(li)
#
# print(heapq.heappop(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
##################################################################

# _list = [1]
#
# print(_list.pop())
# print(_list.pop())