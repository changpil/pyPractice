import queue, threading
import itertools

con = threading.Condition()
done = False
shared_resource = 1
LIMIT_NUM =6

def fizz(con):
    global shared_resource, LIMIT_NUM, done
    while True:
        con.acquire()
        if done:
            con.wait()
        if shared_resource == None:
            con.notifyAll()
            con.release()
            break
        if shared_resource % 3 == 0 and shared_resource % 5 != 0:
            print("{} fizz".format(shared_resource))
            done = True
            con.notifyAll()
        con.release()
    print("DONE fizz")

def buzz(con):
    global shared_resource, LIMIT_NUM, done
    while True:
        con.acquire()
        if done:
            con.wait()
        if shared_resource == None:
            con.notifyAll()
            con.release()
            break
        if shared_resource % 3 != 0 and shared_resource % 5 == 0:
            print("{} buzz".format(shared_resource))
            done = True
            con.notifyAll()
        con.release()
    print("DONE buzz")


def fizzbuzz(con):
    global shared_resource, LIMIT_NUM, done
    while True:
        con.acquire()
        if done:
            con.wait()
        if shared_resource == None:
            con.notifyAll()
            con.release()
            break
        if shared_resource % 3 == 0 and shared_resource % 5 == 0:
            print("{} fizzbuzz".format(shared_resource))
            done = True
            con.notifyAll()
        con.release()
    print("DONE fizzbuzz")


def number(con):
    global shared_resource, LIMIT_NUM, done
    while True:
        con.acquire()
        if done:
            con.wait()
        if shared_resource == None:
            done= False
            con.notifyAll()
            con.release()
            break
        if shared_resource % 3 != 0 and shared_resource % 5 != 0:
            print("{}".format(shared_resource))
            done = True
            con.notifyAll()
        con.release()
    print("Done number")



t1 = threading.Thread(target= fizz, args=(con, ))
t2 = threading.Thread(target= buzz, args=(con, ))
t3 = threading.Thread(target= fizzbuzz, args=(con, ))
t4 = threading.Thread(target= number, args=(con, ))




t1.start()
t2.start()
t3.start()
t4.start()

while True:

    con.acquire()
    if not done:
        con.wait()
    done = False
    shared_resource += 1
    if shared_resource > LIMIT_NUM:
        print("shared_resource == None")
        shared_resource = None
        con.notifyAll()
        con.release()
        break
    con.notifyAll()
    con.release()

print("Pattern1:knapsack.join {}".format(shared_resource))
t1.join()
print("2.join")
t2.join()
print("3.join")
t3.join()
print("4.join")
t4.join()

print("end of main")