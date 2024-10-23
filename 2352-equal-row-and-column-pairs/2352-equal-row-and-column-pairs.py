class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows: dict[int, list[int]] = dict()
        columns: dict[int, list[int]] = dict()
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i not in rows.keys():
                    rows[i] = []
                
                if j not in columns.keys():
                    columns[j] = []
                
                rows[i].append(grid[i][j])
                columns[j].append(grid[i][j])
        
        count: int = 0
        for i in rows.values():
            for j in columns.values():
                if i == j:
                    count += 1
        
        return count
        
        