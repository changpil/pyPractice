class Heap:

    def __init__(self, size=10, reversed= False):
        self._list=[None]
        self.size = size
        self.reversed = -1 if reversed == True else 1

    def put(self, priority, item):
        if self.size == len(self._list):
            raise IndexError

        self._list.append((self.reversed*priority, item))
        last_p = len(self._list) - 1

        while last_p != 1:
            if self._list[last_p][0] < self._list[last_p//2][0]:
                self._list[last_p//2], self._list[last_p] = self._list[last_p], self._list[last_p // 2]
            last_p = last_p//2
        #print(self._list)

    def get(self):
        if len(self._list) ==0:
            raise IndexError

        return_v = self._list[1][1]
        last_p = len(self._list)-1
        self._list[1], self._list[last_p] = self._list[last_p], self._list[1]
        del self._list[last_p]

        try:
            i = 1
            while True:
                min_p = min(self._list[2*i][0], self._list[2*i+1][0])
                min_i =  2*1 if self._list[2*i][0] == min_p else 2*i+1
            self._list[i], self._list[min_i] = self._list[min_i], self._list[i]
            i = min_i
        except IndexError:
            pass

        return return_v

    def size(self):
        return self.size;

    def peak(self):
        if len(self._list) ==0:
            raise IndexError
        return self._list[1][1]



heap = Heap(reversed=True)
heap.put(6, "6666")
heap.put(1, "1111")
heap.put(3, "333")
print(heap._list)
print(heap.get())
print(heap.get())