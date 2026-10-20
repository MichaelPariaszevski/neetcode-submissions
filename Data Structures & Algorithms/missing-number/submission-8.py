class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        for i in range(len(nums)): 
            result = result ^ nums[i]
            result = result ^ i

        return result
            

        