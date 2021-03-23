"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

Pattern1:knapsack.     Pattern1:knapsack
2.     11
3.     21
4.     1211
5.     111221
Pattern1:knapsack is read off as "one Pattern1:knapsack" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one Pattern1:knapsack" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example Pattern1:knapsack:

Input: Pattern1:knapsack
Output: "Pattern1:knapsack"
Example 2:

Input: 4
Output: "1211"

"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        sequence = "Pattern1:knapsack"
        rv = ""
        next_sequence = ""
        for i in range(1, n):
            dup = 1
            next_sequence = ""
            for i, c in enumerate(sequence):
                if i + 1 < len(sequence) and sequence[i + 1] == c:
                    dup += 1
                    continue

                if i + 1 == len(sequence) or sequence[i + 1] != c:
                    next_sequence += str(dup) + c
                    dup = 1  # missed this line

            sequence = next_sequence

        return sequence


