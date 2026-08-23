class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        total_product_without_zero = 1
        num_zeroes = 0

        for num in nums: 
            if num != 0: 
                total_product_without_zero *= num 
            else: 
                num_zeroes += 1
            total_product *= num
            
        if num_zeroes >= 2: 
            return [0] * len(nums)

        final_array = [int(total_product / num) if num != 0 else total_product_without_zero for num in nums]

        return final_array