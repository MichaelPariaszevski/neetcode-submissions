class Node: 
    def __init__(self): 
        self.children: list[str, Node | str] = {}
        self.word: str | None = None

class Trie: 
    def __init__(self): 
        self.root = Node()

class Solution:
    def __init__(self): 
        self.trie = Trie()
        self.board: List[List[str]] = []
        self.result: List[str] = []
        self.num_rows: int
        self.num_columns: int

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board

        for word in words: 
            curr_level = self.trie.root
            for char in word: 
                if char not in curr_level.children: 
                    curr_level.children[char] = Node()
                curr_level = curr_level.children[char]

            curr_level.word = word

        self.num_rows = len(board)
        self.num_columns = len(board[0])

        for row in range(self.num_rows): 
            for column in range(self.num_columns): 
                self.dfs(row, column, self.trie.root)

        return list(set(self.result))

    def dfs(self, row: int, column: int, curr_node: Node) -> str | None: 
        if row < 0 or row >= self.num_rows or column < 0 or column >= self.num_columns or self.board[row][column] == "#" or self.board[row][column] not in curr_node.children: 
            return None

        new_node = curr_node.children[self.board[row][column]]

        if new_node.word is not None: 
            self.result.append(new_node.word)

        saved_value = self.board[row][column]
        self.board[row][column] = "#"

        self.dfs(row - 1, column, new_node)
        self.dfs(row + 1, column, new_node)
        self.dfs(row, column - 1, new_node)
        self.dfs(row, column + 1, new_node)

        self.board[row][column] = saved_value



        

