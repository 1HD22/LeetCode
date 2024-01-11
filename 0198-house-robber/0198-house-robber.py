class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        larger = lambda a,b: a if a>b else b
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        arr = [0 for i in nums]
        
        arr[0] = nums[0]
        arr[1] = larger(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            arr[i] = larger(arr[i-2]+nums[i], arr[i-1])
            
        return arr[n-1]

#