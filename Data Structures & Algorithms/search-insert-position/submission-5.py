# The left pointer always moves past elements smaller than the target, 
# stopping exactly where the target should go.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < len(nums) and left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target: 
                return mid 
            elif nums[mid] > target: 
                right = mid - 1 
            else: 
                left = mid + 1

        return left