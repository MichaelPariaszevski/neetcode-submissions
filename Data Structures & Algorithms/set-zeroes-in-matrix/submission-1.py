class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        visited_row: Set[int] = set()
        visited_col: Set[int] = set()

        for row in range(len(matrix)): 
            for col in range(len(matrix[0])): 
                if matrix[row][col] == 0: 
                    visited_row.add(row)
                    visited_col.add(col)

        for row in range(len(matrix)): 
            for col in range(len(matrix[0])): 
                if row in visited_row or col in visited_col: 
                    matrix[row][col] = 0

        
        