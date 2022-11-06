class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if (low % 2 and high % 2):
            return int((high - low)/2 + 1)
        elif (not(low % 2) and high % 2):
            return int((high - low - 1) / 2 + 1)
        elif (low % 2 and not(high % 2)):
            return int((high - low - 1) / 2 + 1)
        elif (not(low % 2) and not(high % 2)):
            return int((high - low) / 2)
        
        return 0
            
        