class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 1
        maximum = 0
        
        while sell < len(prices):
            
            maximum = max(maximum, prices[sell]-prices[buy])
            
            if prices[sell] < prices[buy]:
                buy = sell
            
            sell += 1
        
        return maximum