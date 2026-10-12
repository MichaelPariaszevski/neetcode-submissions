class Solution:
    def __init__(self): 
        self.memo: Dict[int, int] = {}
        self.string: str
        self.mapping: Set[str] = set()

    def numDecodings(self, s: str) -> int:
        for num in range(10, 27): 
            self.mapping.add(str(num))

        self.string = s

        return self.dfs(0)

    def dfs(self, index: int): 
        if index > len(self.string): 
            return 0
        elif index in self.memo: 
            return self.memo[index]
        elif index == len(self.string): 
            return 1
        
        one_step = 0
        two_step = 0

        if self.string[index] != "0": 
            one_step = self.dfs(index + 1)
        if index + 2 <= len(self.string) and self.string[index : index + 2] in self.mapping: 
            two_step = self.dfs(index + 2)

        total_ways = one_step + two_step

        self.memo[index] = total_ways

        return total_ways

            
        