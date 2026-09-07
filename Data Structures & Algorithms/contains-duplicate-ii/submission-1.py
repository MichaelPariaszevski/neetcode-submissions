class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # arr = []
        if len(nums) <= 1: 
            return False 

        curr_values = {}
        left, right = 0, 0

        for i in range(k + 1): 
            # arr.append(nums[right])
            if curr_values.get(nums[right], 0) == 1: 
                return True
            curr_values[nums[right]] = 1
            right += 1
            if right >= len(nums): 
                return False

        while right < len(nums): 
            curr_values.pop(nums[left])
            if curr_values.get(nums[right], 0) == 1: 
                return True
            curr_values[nums[right]] = 1
            left += 1
            right += 1

        return False

