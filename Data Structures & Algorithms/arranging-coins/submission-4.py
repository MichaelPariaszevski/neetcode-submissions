class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n

        while left <= right: 
            mid = (left + right) // 2
            curr_result = (mid * (mid + 1)) / 2
            if curr_result == n: 
                return mid 
            elif curr_result > n: 
                right = mid - 1
            else: 
                left = mid + 1

        return right