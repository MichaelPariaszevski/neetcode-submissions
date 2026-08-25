class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        len_nums = len(nums)

        for i in nums: 
            hash_map[i] = hash_map.get(i, 0) + 1

        for key, value in hash_map.items(): 
            if value >= len_nums // 2: 
                return key
        