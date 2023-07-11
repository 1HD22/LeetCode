class Solution:
    def removeStack(self, index: int) -> None:
        if index == 0:
            self.length -= 1
            self.nums[:self.length] = self.nums[1:self.length+1]
            
        elif index == len(self.nums)-1:
            self.length -= 1
        
        else:
            self.length -= 1
            self.nums[index:self.length] = self.nums[index+1:self.length+1]
            
        
    def removeElement(self, nums: List[int], val: int) -> int:
        self.nums = nums
        self.length = len(nums)
        self.val = val
        
        i = 0
        while i < self.length:
            
            if self.nums[i] == val:
                self.removeStack(i)
            else:
                i += 1

        nums = self.nums
        return self.length

        