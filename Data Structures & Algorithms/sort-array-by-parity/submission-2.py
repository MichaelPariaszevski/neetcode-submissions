class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right: 
            if nums[left] % 2 != 0 and nums[right] % 2 == 0: 
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                left += 1
                right -= 1
            elif nums[left] % 2 == 0 and nums[right] % 2 != 0: 
                left += 1
                right -= 1
            elif nums[left] % 2 == 0 and nums[right] % 2 == 0: 
                left += 1
            else: 
                right -= 1

        return nums
        