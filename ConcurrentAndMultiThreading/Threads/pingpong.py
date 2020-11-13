import threading, time

number = 1
con = threading.Condition()
LIMIT = 20

def even():
    global number, con, LIMIT
    while True:
        con.acquire()
        if number > LIMIT:
            con.notifyAll()
            #####an awakened thread does not actually return from its wait() call until it can reacquire the lock.
            con.release()  ##############Important
            ##########################################################
            break
        if number%2 !=0:
            print("even wait()")
            con.wait()
        number += 1
        con.notifyAll()
        con.release()
    print("even is done")


def odd():
    global number, con, LIMIT
    while True:
        con.acquire()
        if number > LIMIT:
            con.notifyAll()
            #####an awakened thread does not actually return from its wait() call until it can reacquire the lock.
            con.release() ##############Important
            ##########################################################
            break
        if number %2 == 0:
            print("odd wait()")
            con.wait()
        number += 1
        con.notifyAll()
        con.release()
    print("odd is done")

t1 = threading.Thread(target=even)
t1.start()
t2 = threading.Thread(target=odd)
t2.start()

t1.join()
t2.join()

print("end of main")