class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1: 
            return len(nums) 

        left, right = 0, 1

        while right < len(nums): 
            if nums[left] == nums[right]: 
                right += 1
            else: 
                if right - left > 1: 
                    nums[left + 1] = nums[right]
                right += 1
                left += 1
            
        nums = nums[:left + 1]

        return left + 1
        