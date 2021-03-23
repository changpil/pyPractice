"""
Most Visited pages
You are given a log file  containing billions of entries. Each entry contains timestamp and page (string).
Implement the following  methods

void add(entry p)
list<string> common(k): return all pages that has more than k frequencies

"""

class LogPages:
    class Entry:
        def __init__(self, log, timestamp, freq =0):
            self.log = log
            self.timestamp = timestamp
            self.freq = freq

    def __init__(self, path):
        self.path = path
        self.load()

    def load(self):
        self.lib = dict()
        with open(self.path,"rt") as f:
            for line in f:
                words = list(line.split())
                _ts = " ".join(words[:3])
                _os = words[4]
                _title = words[5][:-1]
                _session = words[6][:-1]
                _log = " ".join( words[7:])
                self.add(LogPages.Entry(_log, _ts, 1 ))

    def add(self, p):
        entry = self.lib.get(p.log, None)
        if entry != None:
            p.freq += entry.freq + 1
        self.lib[p.log] = p

    def common(self, k):
        pass

cp = LogPages("log.txt")
print(cp.lib)




