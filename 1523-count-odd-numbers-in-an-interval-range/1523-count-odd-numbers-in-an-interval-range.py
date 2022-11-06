class Solution:
    def countOdds(self, low: int, high: int) -> int:
        between = high - low - 1
        
        if (low % 2 == 1 and high % 2 == 1):
            return int((between - 1)/2 + 2)
        elif (low % 2 == 0 and high % 2 == 1):
            return self.countOdds(low+1, high)
        elif (low % 2 == 1 and high % 2 == 0):
            return self.countOdds(low, high-1)
        elif (low % 2 == 0 and high % 2 == 0):
            return self.countOdds(low + 1, high - 1)
        
        return -1
            
        