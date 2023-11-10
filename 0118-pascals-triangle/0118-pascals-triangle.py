class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return list()
        ans = [[0 for i in range(numRows)] for j in range(numRows)]
        
        ans[0][0] = 1
        final = [[1]]
        
        for j in range(1, numRows):
            temp = []
            for i in range(j+1):
                
                if i == 0 or i == j:
                    ans[i][j] = 1
                    temp.append(1)
                    continue
                
                ans[i][j] = ans[i][j-1] + ans[i-1][j-1]
                temp.append(ans[i][j-1]+ans[i-1][j-1])
            final.append(temp)
                
        return final