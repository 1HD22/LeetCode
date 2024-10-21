class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows: set[int] = set()
        columns: set[int] = set()
        m: int = len(matrix)
        n: int = len(matrix[0])
            
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        

        for r in rows:
            for j in range(n):
                matrix[r][j] = 0
                
        for i in range(m):
            for c in columns:
                matrix[i][c] = 0
                