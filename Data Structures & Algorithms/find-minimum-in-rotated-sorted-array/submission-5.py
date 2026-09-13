class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        lowest = nums[left]

        while left <= right: 
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else: 
                lowest = min(lowest, nums[mid])
                right = mid - 1

        return lowest        