class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:
            temp = num
            total = 0
            while temp >= 10:
                total += temp % 10
                temp = (temp - (temp % 10)) / 10
            num = total + temp
        
        return int(num)
            
        
        