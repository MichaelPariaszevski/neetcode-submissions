class Solution:
    def __init__(self): 
        self.memo: Dict[int, int] = {}
        self.nums: List[int]

    def rob(self, nums: List[int]) -> int:
        self.nums = nums

        result = 0

        for i in range(len(nums)): 
            curr_result = self.dfs(i)
            if curr_result > result: 
                result = curr_result

        return result

    def dfs(self, index: int): 
        if index >= len(self.nums): 
            return 0

        if index in self.memo: 
            return self.memo[index]

        value = max(self.nums[index] + self.dfs(index + 2), self.dfs(index + 1))

        self.memo[index] = value

        return value
