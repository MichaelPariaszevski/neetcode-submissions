class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        len_nums = len(nums)

        for num in nums: 
            new_value = hash_map.get(num, 0) + 1
            hash_map[num] = new_value
            if new_value > len_nums // 2: 
                return num
