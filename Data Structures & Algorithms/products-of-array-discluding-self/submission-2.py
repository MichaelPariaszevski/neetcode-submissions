class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # [1, 2, 4, 6]
        # [0, 1, 2, 8]
        # [48, 24, 6, 0]

        pref_suff_arr = [0] * len(nums)

        for i in range(len(nums)): 
            if i == 0: 
                pref_suff_arr[i] = 1
                continue

            pref_suff_arr[i] = nums[i - 1] * pref_suff_arr[i - 1]

        curr_suffix = 1

        for i in range(len(nums) - 1, -1, -1): 
            if i == len(nums) - 1: 
                continue

            curr_suffix *= nums[i + 1]
            pref_suff_arr[i] *= curr_suffix

        return pref_suff_arr

             
        