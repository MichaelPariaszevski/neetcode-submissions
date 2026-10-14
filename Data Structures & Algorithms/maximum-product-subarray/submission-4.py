class Solution:
    def __init__(self): 
        self.nums: List[int]

    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        global_max = nums[0]

        for num in nums[1:]: 
            new_curr_max = curr_max * num
            new_curr_min = curr_min * num

            curr_max = max(num, new_curr_max, new_curr_min)
            curr_min = min(num, new_curr_max, new_curr_min)
            global_max = max(global_max, curr_max)

        return global_max