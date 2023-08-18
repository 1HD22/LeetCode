class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while True:
            
            if n <= 0 or n == 2:
                return False
            elif n == 1:
                return True
            
            new = n // 3
            
            if new * 3 != n:
                return False
            
            n = new
            continue
            
        