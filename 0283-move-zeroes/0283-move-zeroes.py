class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return
        
        zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
        count = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[count] = nums[j]
                count += 1
            
            if j >= len(nums) - zero:
                nums[j] = 0
#
                    
        