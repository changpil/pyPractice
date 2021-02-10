import random


class RandomWeitedIndexPick:

    def __init__(self, w):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self):
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i

r = RandomWeitedIndexPick([1, 3])
for _ in range(24):
    print(r.pickIndex(), end=" ")

print()

r = RandomWeitedIndexPick([1, 10])
for _ in range(24):
    print(r.pickIndex(), end=" ")

print()
r = RandomWeitedIndexPick([500, 10])
for _ in range(24):
    print(r.pickIndex(), end=" ")