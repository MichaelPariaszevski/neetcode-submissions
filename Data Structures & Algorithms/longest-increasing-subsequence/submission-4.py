class Solution:
    def __init__(self): 
        self.nums: List[int]
        self.memo: Dict[int, int] = {}

    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}

        result = 0

        for index in range(len(nums)): 
            curr_res = self.dfs(index)
            if curr_res > result: 
                result = curr_res

        return result

    def dfs(self, index: int): 
        if index == len(self.nums) - 1: 
            return 1
        elif index in self.memo: 
            return self.memo[index]

        result_list: List[int] = []
        
        for new_index in range(index + 1, len(self.nums)): 
            if self.nums[new_index] > self.nums[index]: 
                result_list.append(1 + self.dfs(new_index))

        max_of_result_list = max(result_list) if len(result_list) > 0 else 1
        self.memo[index] = max_of_result_list

        return max_of_result_list
        

        

        

    
        