class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        ans = [0] * (2 * len_nums)

        for index, num in enumerate(nums): 
            ans[index] = num
            ans[index + len_nums] = num

        return ans