class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[-1] = digits[-1] + 1
        
        i = -1;
        while (i >= -n and digits[i] > 9):
            print(i-1, -n)
            if i-1 < -n:
                digits.insert(0,1)
                digits[i] = 0
                break
            else:
                digits[i - 1] = digits[i - 1] + 1
                digits[i] = 0
            
            i = i - 1
        
        return digits
                
        
        