# Using hash set

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_set = set(nums)

        for num in range(len(nums) + 1): 
            if num not in hash_set: 
                return num