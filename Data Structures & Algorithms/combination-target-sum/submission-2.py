class Solution:
    def __init__(self): 
        self.result: List[List[int]] = []
        self.target: int
        self.nums: List[int]
        self.len_nums: int 

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.nums = nums
        self.len_nums = len(nums)

        self.backtrack(0, [], 0)

        return self.result

    def backtrack(self, curr_index: int, current_combo: List[int], current_sum: int): 
        if current_sum == self.target:
            self.result.append(current_combo.copy())
            return 
        elif current_sum > self.target: 
            return 

        for i in range(curr_index, self.len_nums): 
            current_combo.append(self.nums[i])
            current_sum += self.nums[i]
            self.backtrack(i, current_combo, current_sum)
            current_sum -= self.nums[i]
            current_combo.pop()
            
        