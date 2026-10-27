class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result: int = 0
        left, right = 0, 0

        while right < len(nums): 
            if nums[left] == 0: 
                left += 1
                right += 1
            else: 
                while right < len(nums) and nums[right] == 1: 
                    right += 1
                curr_len = right - left
                result = max(result, curr_len)
                left = right
                
        return result
        