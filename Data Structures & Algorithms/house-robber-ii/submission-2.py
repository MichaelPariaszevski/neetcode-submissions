# Think of houses in this problem as either
# from [0 : n - 1], non-inclusive
# or from [1 : n], also non-inclusive

class Solution:
    def __init__(self): 
        self.nums: List[int]
        self.memo: Dict[int, int] = {}

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]

        self.nums = nums

        first_result = self.dfs(0, len(nums) - 1)

        self.memo = {}

        second_result = self.dfs(1, len(nums))

        return max(first_result, second_result)

    def dfs(self, index: int, final_index: int):
        if index >= final_index: 
            return 0 
        elif index in self.memo: 
            return self.memo[index]

        curr_result = max(self.nums[index] + self.dfs(index + 2, final_index), self.dfs(index + 1, final_index)) 

        self.memo[index] = curr_result

        return curr_result


        