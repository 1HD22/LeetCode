class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                count = count + 1
            if nums[i] == val:
                for j in range(i+1,len(nums)):
                    if nums[j] != val:
                        count = count + 1
                        nums[i] = nums[j]
                        nums[j] = val
                        break
        return count