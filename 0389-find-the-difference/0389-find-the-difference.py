class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            print(s)
            if i not in s:
                return i
            s = s.replace(i, '0', 1)
            