class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        count: dict = dict()
            
        for i in arr:
            if i not in count.keys():
                count[i] = 1
                continue
            
            count[i] += 1
            
        occurance: dict = dict()
            
        for val in count.values():
            if val not in occurance.keys():
                occurance[val] = 1
                continue
            
            return False
        
        return True
            