class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        n = str(bin(n))
        
        for i in range(2,len(n)):
            if (n[i] == '0'):
                continue
            sum += 1
        
        return sum