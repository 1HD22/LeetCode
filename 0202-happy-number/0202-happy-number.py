class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n in [2,3,4,5,6,8,9]:
            return False
        
        sum = 0
        n = str(n)
        for i in range(len(n)):
            sum += int(n[i]) ** 2
        
        return self.isHappy(sum)