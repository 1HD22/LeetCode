class Solution:
    def countOdds(self, low: int, high: int) -> int:
        between = high - low - 1
        
        if (low % 2 == 1 and high % 2 == 1):
            return int((between - 1)/2 + 2)
        elif (low % 2 == 0 and high % 2 == 1):
            return int(between / 2 + 1)
        elif (low % 2 == 1 and high % 2 == 0):
            return int(between / 2 + 1)
        elif (low % 2 == 0 and high % 2 == 0):
            return int((between + 1) / 2)
        
        return -1
            
        