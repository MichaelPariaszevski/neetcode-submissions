class Solution:
    def __init__(self): 
        self.grid: List[List[str]]
        self.num_rows: int 
        self.num_columns: int 
        self.result: int = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.num_rows = len(grid)
        self.num_columns = len(grid[0])

        for row in range(self.num_rows): 
            for column in range(self.num_columns): 
                if self.dfs(row, column) is not None: 
                    self.result += 1

        return self.result
                

    def dfs(self, row: int, column: int) -> bool | None: 
        if row < 0 or row >= self.num_rows or column < 0 or column >= self.num_columns or self.grid[row][column] == "#" or self.grid[row][column] == "0": 
            return None
        
        self.grid[row][column] = "#"
        
        self.dfs(row - 1, column)
        self.dfs(row + 1, column)
        self.dfs(row, column - 1)
        self.dfs(row, column + 1)

        return True