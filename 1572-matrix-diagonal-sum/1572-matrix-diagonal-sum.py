class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        j = len(mat) - 1
        for i in range(len(mat)):
            sum += mat[i][i]
            if i != j:
                sum += mat[i][j]
            j -= 1
        
        return sum
            
#1