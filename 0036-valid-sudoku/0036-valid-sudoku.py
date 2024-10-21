class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n: int = len(board)
        column: dict[int, list[int]] = {i: list() for i in range(n)}
        row: dict[int, list[int]] = {i: list() for i in range(n)}
        subbox: dict[int, list[int]] = {i: list() for i in range(n)}

            
        for i in range(n):
            for j in range(n):
                
                if board[i][j] == '.':
                    continue
                
                val: int = int(board[i][j])
                    
                if val in row[i]:
                    return False
                
                if val in column[j]:
                    return False
                
                box: int = (i // 3) * 3  + j // 3
                if val in subbox[box]:
                    return False
                
                row[i].append(val)
                column[j].append(val)
                subbox[box].append(val)
        
        return True
        