class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        for num in nums: 
            if num != counter: 
                return counter
            counter += 1

        return counter
        
        