class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negative_arr: List[int] = []
        full_arr: List[int] = []

        for i in range(len(nums)): 
            if nums[i] < 0: 
                negative_arr.append(nums[i])
            else: 
                while negative_arr and abs(negative_arr[-1]) <= abs(nums[i]): 
                    full_arr.append(negative_arr[-1] ** 2)
                    negative_arr.pop(-1)
                full_arr.append(nums[i] ** 2)

        if negative_arr: 
            for i in range(len(negative_arr) - 1, -1, -1): 
                full_arr.append(negative_arr[i] ** 2)

        return full_arr

        

        