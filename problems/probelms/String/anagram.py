class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i in s:
            data = d.get(i, [0, 0])
            data[0] = data[0] + 1
            d[i] = data

        for i in t:
            data = d.get(i, [0, 0])
            data[1] = data[1] + 1
            d[i] = data

        for v in d.values():
            if v[0] != v[1]:
                return False
        return True

a="a"
b="aa"
s=Solution()
print(s.isAnagram(a,b))