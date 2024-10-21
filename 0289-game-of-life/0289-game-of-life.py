class Solution:
    def insert(self, i: int, j: int, counter: List[List[int]]):
        possible: List[Tuple[int]] = [(i-1, j-1), (i-1, j), (i-1, j+1),
                                     (i, j-1),               (i, j+1),
                                     (i+1, j-1), (i+1, j), (i+1, j+1)]
        
        for a, b in possible:
            if a < 0 or a >= self.m:
                continue
            if b < 0 or b >= self.n:
                continue
            
            counter[a][b] += 1
            
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m: int = len(board)
        self.n: int = len(board[0])
        live: List[List[int]] = [[0 for _ in range(self.n)] for _ in range(self.m)]
            
        for i in range(self.m):
            for j in range(self.n):
                
                if board[i][j] == 1:
                    self.insert(i, j, live)
        
        for i in range(self.m):
            for j in range(self.n):
                
                if board[i][j] == 1:
                    if live[i][j] < 2 or live[i][j] > 3:
                        board[i][j] = 0
                else:
                    if live[i][j] == 3:
                        board[i][j] = 1
                    
                        