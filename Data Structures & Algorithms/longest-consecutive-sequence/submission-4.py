class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: 
            return len(nums)

        nums_set = set(nums)
        longest = 0

        for num in nums: 
            if (num - 1) not in nums_set: 
                i = 1
                curr_len = 1
                while (num + i) in nums_set: 
                    curr_len += 1
                    i += 1
                longest = max(longest, curr_len)

        return longest


