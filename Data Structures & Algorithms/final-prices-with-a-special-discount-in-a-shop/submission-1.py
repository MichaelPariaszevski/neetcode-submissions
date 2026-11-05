class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack: List[Tuple[int, int]] = [(prices[0], 0)]

        for i in range(1, len(prices)): 
            while len(stack) > 0 and prices[i] <= stack[-1][0]: 
                prices[stack[-1][1]] = stack[-1][0] - prices[i]
                stack.pop(-1)
            stack.append((prices[i], i))

        return prices

        

