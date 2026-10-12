class Solution:
    def __init__(self): 
        self.string: str
        self.mapping: Set[str]
        self.result: int = 0
        self.memo: Dict[int, Dict[int, int]] = {}

    def numDecodings(self, s: str) -> int:
        mapping: Set[str] = set()
        
        for num in range(26): 
            mapping.add(str(num + 1))

        self.string = s
        self.mapping = mapping

        self.dfs(0, 1)
        self.dfs(0, 2)

        return self.result

    def dfs(self, start_index: int, end_index: int): 
        if start_index in self.memo and end_index in self.memo[start_index]: 
            self.result += self.memo[start_index][end_index]
            return self.memo[start_index][end_index]
        elif end_index > len(self.string): 
            return 0
        elif self.string[start_index : end_index] not in self.mapping: 
            return 0
        elif end_index == len(self.string): 
            self.result += 1
            return 1

        curr_result = self.dfs(end_index, end_index + 1) + self.dfs(end_index, end_index + 2)

        if start_index not in self.memo: 
            self.memo[start_index] = {}
        self.memo[start_index][end_index] = curr_result

        return curr_result