class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        print(type(self))
        return f"SimpleList ({self._items})"

class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().__init__(item)
        self.sort()

    def __repr__(self):
        print(type(self))
        return f"SortedList ({list(self)})"

class IntList(SimpleList):
    def __init__(self, items =()):
        for x in items:
            self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise ValueError("IntList only supports integer values.")

    def add(self, item):
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return "IntList ({list(self})"

class SortedIntList(IntList, SortedList):
    # MRO for SortedIntList
    # SortedIntList Search for methods name for add in subclass
    # IntList  --> super().add will continue to SimpleList to get down to next MRO
    # SimpleList --> super().add
    # Object


    def __repr__(self):
        print(type(self))
        return f"SortedIntList ({list(self)})"

sl = SimpleList([4,5,-6, 0])
print(sl)
sl = SortedList([4,5,-6, 0])
print(sl)
try:
    sl = IntList([4,2,7,6.7])
except ValueError as e:
    print(e)
print(sl)

sl = SortedIntList([3,-5, 6, -7])
print(sl)

print(SortedIntList.__bases__)
print(SortedIntList.__mro__)
print(SortedIntList.mro())