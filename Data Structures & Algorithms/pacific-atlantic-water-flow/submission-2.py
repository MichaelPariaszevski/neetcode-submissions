class Solution:
    def __init__(self): 
        self.board: List[List[int]]
        self.num_rows: int 
        self.num_columns: int 
        self.pac_visited: set[tuple[int]] = set()
        self.atl_visited: set[tuple[int]] = set()
        self.result: List[List[int]] = []

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.board = heights

        self.num_rows = len(heights)
        self.num_columns = len(heights[0])

        for row in range(self.num_rows): 
            self.dfs(row, 0, -1, self.pac_visited)

        for column in range(self.num_columns): 
            self.dfs(0, column, -1, self.pac_visited)

        for row in range(self.num_rows): 
            self.dfs(row, self.num_columns - 1, -1, self.atl_visited)

        for column in range(self.num_columns): 
            self.dfs(self.num_rows - 1, column, -1, self.atl_visited)

        for entry_pac in self.pac_visited: 
            if entry_pac in self.atl_visited: 
                self.result.append(list(entry_pac))

        return self.result

    def dfs(self, row: int, column: int, prev_height: int, visited_set: set[tuple[int]]): 
        if row < 0 or row >= self.num_rows or column < 0 or column >= self.num_columns or self.board[row][column] < prev_height: 
            return 

        if (row, column) not in visited_set: 
            visited_set.add((row, column))
        else: 
            return 

        recorded_value = self.board[row][column]

        self.dfs(row + 1, column, recorded_value, visited_set)
        self.dfs(row - 1, column, recorded_value, visited_set)
        self.dfs(row, column + 1, recorded_value, visited_set)
        self.dfs(row, column - 1, recorded_value, visited_set)
    
        return

