class Solution:
    def hammingWeight(self, n: int) -> int:
        power = 0
        sum = 0
        
        while (2**power < n):
            power += 1
        
        while (n != 0 or power >= 0):
            if (n - 2 ** power >= 0):
                n = n - 2 ** power
                sum += 1
            power -= 1
        
        return sum
