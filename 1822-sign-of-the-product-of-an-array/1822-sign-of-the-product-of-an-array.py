class Solution:
    def signFunc(self, num: int) -> int:
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0
        
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for i in range(len(nums)):
            sign *= self.signFunc(nums[i])
            if sign == 0:
                return 0
        
        return sign
        