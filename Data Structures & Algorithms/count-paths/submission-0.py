class Solution:
    def __init__(self): 
        self.memo: Dict[tuple[int, int], int] = {}
        self.m: int
        self.n: int

    def uniquePaths(self, m: int, n: int) -> int:
        self.m = m
        self.n = n
        self.memo = {}

        return self.dfs(0, 0)

    def dfs(self, curr_m: int, curr_n: int) -> int: 
        if curr_m < 0 or curr_n < 0: 
            return 0
        elif curr_m >= self.m or curr_n >= self.n: 
            return 0
        elif (curr_m, curr_n) in self.memo: 
            return self.memo[(curr_m, curr_n)]
        elif curr_m == self.m - 1 and curr_n == self.n - 1: 
            return 1

        right = self.dfs(curr_m + 1, curr_n)
        down = self.dfs(curr_m, curr_n + 1)

        value = right + down

        self.memo[(curr_m, curr_n)] = value

        return value

        
        