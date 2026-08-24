class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: 
            return 0

        curr_ptr = 0
        counter = 0

        for i in range(len(nums)): 
            if nums[i] != val: 
                nums[curr_ptr] = nums[i]
                counter += 1
                curr_ptr += 1

        return counter

        