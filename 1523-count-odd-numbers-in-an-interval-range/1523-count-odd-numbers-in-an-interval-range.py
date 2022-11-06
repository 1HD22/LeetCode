class Solution:
    def countOdds(self, low: int, high: int) -> int:
        between = high - low - 1
        low = low % 2
        high = high % 2
        
        if (low == 1 and high == 1):
            return int((between - 1)/2 + 2)
        elif (low == 0 and high == 1):
            return int(between / 2 + 1)
        elif (low == 1 and high == 0):
            return int(between / 2 + 1)
        elif (low == 0 and high == 0):
            return int((between + 1) / 2)
        
        return -1
            
        