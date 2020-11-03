import threading, time

class Basic_t(threading.Thread):
    def __init__(self, t, text):
        super().__init__()
        self.t = t
        self.txt =text

    def do_some_work(self, t, txt):
        print("doing some work in thread {}".format(txt))
        time.sleep(t)
        print("end of thread {}".format(txt))

    def run(self):
        self.do_some_work(self.t, self.txt)

t1 = Basic_t(2, "short T")
t2 = Basic_t(12, "long T")

t1.start()
t2.start()

t1.join()
t2.join()
print("end of main")