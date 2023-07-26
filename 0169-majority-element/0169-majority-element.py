#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
       # initial naive solution. Time: O(n), Space: O(n)
#         count = {}
#         length = len(nums)
        
#         for i in range(length):
#             if nums[i] not in count.keys():
#                 count[nums[i]] = 1
#             else:
#                 count[nums[i]] += 1
            
#             if count[nums[i]] > length // 2:
#                 return nums[i]
            
        
#         return -1

        # Boyer-Moore Majority Voting. Time: O(n), Space: O(1)
        majority = -1
        i = 0
        
        for x in nums:
            if i == 0:
                m=x
                i=1
            elif x == m:
                i += 1
            else:
                i -= 1
        
        return m
        