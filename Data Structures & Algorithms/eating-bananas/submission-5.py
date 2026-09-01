class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = 1
        while left <= right: 
            middle = (left + right) // 2
            if self.rate_is_valid(middle, piles, h): 
                right = middle - 1
                result = middle
            else: 
                left = middle + 1

        return result
        
    def rate_is_valid(self, rate: int, piles: List[int], h: int) -> bool: 
            total_hours = 0
            for i in range(len(piles)): 
                curr_pile = piles[i]
                hours_needed_for_pile = math.ceil(curr_pile / rate)
                total_hours += hours_needed_for_pile

            if total_hours > h: 
                return False
            else: 
                return True

            