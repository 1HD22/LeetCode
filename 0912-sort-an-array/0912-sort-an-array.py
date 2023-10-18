class Solution:
    def checkSorted(self, nums:List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True
    
    def partition(self, nums: List[int]) -> List[int]:
        n = len(nums)
        print(n)
        r = random.randint(0, n-1)
        
        nums[r], nums[n-1] = nums[n-1], nums[r]
        
        i = -1
        for j in range(0, n-1):
            if nums[j] <= nums[n-1]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        nums[n-1], nums[i+1] = nums[i+1], nums[n-1]
        
        return i+1
    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        n = len(nums)
        if n <= 1:
            return nums
        
        if self.checkSorted(nums):
            return nums
        
        i = self.partition(nums)
        nums[0:i] = self.sortArray(nums[0:i])
        nums[i+1:n] = self.sortArray(nums[i+1:n])
        
        return nums
        