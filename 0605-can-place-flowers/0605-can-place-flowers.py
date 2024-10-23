class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0:
            return True
        
        size: int = len(flowerbed)
        count: int = 0
            
        for i in range(size):
            
            if flowerbed[i] == 1:
                continue
            
            if (i-1 >= 0):
                if flowerbed[i-1] == 1:
                    continue
            
            if (i+1 < size):
                if flowerbed[i+1] == 1:
                    continue
            
            count += 1
            flowerbed[i] = 1
            
            if count >= n:
                return True
            
        return False