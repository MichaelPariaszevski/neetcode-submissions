class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left, right = 0, 1

        while right < len(nums): 
            if nums[left] == nums[right]: 
                nums[left] *= 2
                nums[right] = 0
            left += 1
            right += 1

        left, right = 0, 1

        temp_arr = [x for x in nums if x != 0]

        return temp_arr + ([0] * (len(nums) - len(temp_arr)))
