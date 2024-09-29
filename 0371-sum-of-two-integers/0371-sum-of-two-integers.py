class Solution:
    def getSum(self, a: int, b: int) -> int:
        keep = (a & b) << 1
        res = a^b
        
        if keep == 0:
            return res
        
        return add(keep, res)

#1