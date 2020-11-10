class TwoStacks:
    def __init__(self, n):
        self.ss = [None for _ in range(n)]
        self.s1_start, self.s1_end = -1, 0
        self.s2_start, self.s2_end = len(self.ss), len(self.ss) -1

    def push1(self, v):
        if self.s1_start +1 < self.s2_start:
            self.ss[self.s1_start +1] =v
            self.s1_start += 1
        else:
            raise
    def pop1(self):
        if self.s1_start < 0:
            raise
        v = self.ss[self.s1_start]
        self.ss[self.s1_start] = None
        self.s1_start -= 1
        return v

    def push2(self, v):
        if self.s2_start - 1 > self.s1_start:
            self.ss[self.s2_start -1] =v
            self.s2_start -= 1
        else:
            raise
    def pop2(self):
        if self.s2_start >= len(self.ss):
            raise
        v = self.ss[self.s2_start]
        self.ss[self.s2_start] = None
        self.s2_start += 1
        return v

    def __str__(self):
        s = ""
        for i in self.ss:
            s += f"{i} "
        return s
    
ss = TwoStacks(10)
ss.push1(1)
ss.push2(10)
print(ss)
ss.push1(4)
ss.push2(6)
print(ss)
ss.pop1()
print(ss)
