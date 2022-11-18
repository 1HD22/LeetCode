class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            ans = -int(''.join(reversed(str(-x))))
        else:
            ans = int(''.join(reversed(str(x))))
        
        if ans < -2**31 or ans > 2**31 - 1:
            print(ans < -2**31, ans > 2**31 - 1)
            return 0
        
        return ans