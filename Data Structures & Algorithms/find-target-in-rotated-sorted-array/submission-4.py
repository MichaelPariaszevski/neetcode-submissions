class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        lowest = nums[left]
        lowest_index = left

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: 
                return mid 
            elif nums[mid] > nums[right]: 
                left = mid + 1
            else: 
                lowest_index = mid if nums[mid] < lowest else lowest_index
                lowest = min(lowest, nums[mid])
                right = mid - 1

        pivot = lowest_index
        left, right = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[right]: 
            left = pivot 
        else: 
            right = pivot - 1

        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target: 
                return mid 
            elif nums[mid] > target: 
                right = mid - 1
            else: 
                left = mid + 1
            

        return -1 


        # 3 4 5 6 1 2 ; target = 4