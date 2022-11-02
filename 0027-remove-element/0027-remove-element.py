class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
        
        count = 0
        for j in range(len(nums)):
            if nums[j] != -1:
                count = count + 1
            else:
                for k in range(j+1,len(nums)):
                    if nums[k] != -1:
                        count = count + 1
                        nums[j] = nums[k]
                        nums[k] = -1
                        print(nums)
                        break
        return count