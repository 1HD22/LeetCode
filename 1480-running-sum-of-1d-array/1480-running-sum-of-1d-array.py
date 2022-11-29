class Solution:
    def sumlist(self, nums, a):
        sum = 0
        for i in range(a+1):
            sum = sum + nums[i]
        return sum
    def runningSum(self, nums: List[int]) -> List[int]:
        return [Solution.sumlist(self, nums, i) for i in range(len(nums))]