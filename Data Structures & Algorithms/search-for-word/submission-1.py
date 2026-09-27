class Solution:
    def __init__(self): 
        self.board: List[List[str]]
        self.word: str
        self.word_len: int
        self.num_rows: int 
        self.num_columns: int 

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.word_len = len(word)
        self.num_rows = len(board)
        self.num_columns = len(board[0])

        for row in range(self.num_rows): 
            for column in range(self.num_columns): 
                if self.backtrack(row, column, 0): 
                    return True

        return False 

    def backtrack(self, row: int , column: int, curr_word_index: int) -> bool: 
        if curr_word_index == self.word_len: 
            return True 
        if row < 0 or row >= self.num_rows or column < 0 or column >= self.num_columns or self.board[row][column] == "#" or self.word[curr_word_index] != self.board[row][column]: 
            return False

        saved_value = self.board[row][column]
        self.board[row][column] = "#"

        if self.backtrack(row - 1, column, curr_word_index + 1) or self.backtrack(row + 1, column, curr_word_index + 1) or self.backtrack(row, column - 1, curr_word_index + 1) or self.backtrack(row, column + 1, curr_word_index + 1): 
            return True 
        else: 
            self.board[row][column] = saved_value
            return False 



        


        