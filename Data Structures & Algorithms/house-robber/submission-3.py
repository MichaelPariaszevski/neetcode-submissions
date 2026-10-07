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
        if index in self.memo: 
            return self.memo[index]

        result_list: List[int] = [0]
        curr_value = self.nums[index]

        for new_index in range(index + 2, len(self.nums)): 
            result_list.append(self.dfs(new_index))

        self.memo[index] = curr_value + max(result_list)

        return self.memo[index]
