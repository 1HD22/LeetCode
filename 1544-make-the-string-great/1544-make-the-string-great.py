class Solution:
    def isbad(self, x:str, y:str) -> bool:
        if ((ord(x) - ord(y)) in [-32,32]):
            return True
        return False
    
    def makeGood(self, s: str) -> str:
        i = 0
        
        while(i < len(s) - 1):
            if (self.isbad(s[i],s[i+1])):
                s = s[:i] + s[i+2:]
                i = -1
            i += 1
            
        return s