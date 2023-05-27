class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        middle = num // 2
        
        while (left <= right):
            middle = (right + left) // 2
            
            square = middle * middle
            
            if (square == num):
                return True
            
            if (square > num):
                right = middle - 1
            else:
                left = middle + 1
            
            
        
        return False