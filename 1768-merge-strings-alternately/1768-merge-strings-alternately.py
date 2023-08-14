class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = list()
        
        for i in range(max(len(word1), len(word2))):
            
            if (i < len(word1)):
                a.append(word1[i])
                
            if (i < len(word2)):
                a.append(word2[i])
        
        return "".join(a)