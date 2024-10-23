class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        n1: set = set(nums1)
        n2: set = set(nums2)
            
        return [list(n1 - n2), list(n2 - n1)]