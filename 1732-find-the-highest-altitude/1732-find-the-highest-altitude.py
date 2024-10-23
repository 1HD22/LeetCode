class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_: int = 0
        mov: int = 0
            
        for g in gain:
            mov += g
            
            if mov > max_:
                max_ = mov
        
        return max_