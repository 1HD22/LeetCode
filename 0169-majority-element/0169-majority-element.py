class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        length = len(nums)
        
        for i in range(length):
            if nums[i] not in count.keys():
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
            
            if count[nums[i]] > length // 2:
                return nums[i]
            
        
        return -1