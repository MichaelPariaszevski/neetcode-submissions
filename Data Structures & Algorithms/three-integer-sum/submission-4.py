class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        start = 0
        end = len(nums) - 1
        while start <= len(nums) - 3: 
            if nums[start] > 0: 
                break

            if start > 0 and nums[start] == nums[start - 1]: 
                start += 1
                continue

            value_needed = -1 * (nums[start])
            left, right = start + 1, end
            while left < right: 
                if nums[left] + nums[right] == value_needed: 
                    list_to_add = [nums[start], nums[left], nums[right]]
                    res.append(list_to_add)
                    left += 1
                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1
                elif nums[left] + nums[right] < value_needed: 
                    left += 1
                else: 
                    right -= 1
            start += 1

        return res