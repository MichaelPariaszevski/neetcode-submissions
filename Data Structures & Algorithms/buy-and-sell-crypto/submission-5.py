class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: 
            return 0

        left, right = 0, 1

        curr_max = 0

        while right < len(prices): 
            curr_diff = prices[right] - prices[left]
            curr_max = max(curr_max, curr_diff)
            
            if prices[right] < prices[left]: 
                left = right
            right += 1

        return curr_max


        