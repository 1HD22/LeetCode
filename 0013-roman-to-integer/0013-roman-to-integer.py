class Solution(object):
    def romanToInt(self, s):
        sum = 0
        now = 0
        previous = 0
        for i in range(-1,-len(s)-1,-1):
        
            if s[i] == 'I':
                now = 1
            elif s[i] == 'V':
                now = 5
            elif s[i] == 'X':
                now = 10
            elif s[i] == 'L':
                now = 50
            elif s[i] == 'C':
                now = 100
            elif s[i] == 'D':
                now = 500
            elif s[i] == 'M':
                now = 1000
            
            if previous > now:
                now = -now
            
            previous = abs(now)
            sum += now
        
        return sum