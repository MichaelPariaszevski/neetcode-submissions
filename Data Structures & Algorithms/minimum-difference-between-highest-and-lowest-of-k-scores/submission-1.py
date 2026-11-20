class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        new_arr = sorted(nums)

        curr_min = float("inf")

        for i in range(len(new_arr) - k + 1): 
            if new_arr[i + k - 1] - new_arr[i] < curr_min: 
                curr_min = new_arr[i + k - 1] - new_arr[i]

        return curr_min

        