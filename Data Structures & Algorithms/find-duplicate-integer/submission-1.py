class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map = {}
        for i in range(len(nums)): 
            if hash_map.get(nums[i]) == 1: 
                return nums[i]
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1