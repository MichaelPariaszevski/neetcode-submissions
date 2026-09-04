class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height = 0

        left, right = 0, len(heights) - 1

        while left < right: 
            curr_height = (right - left) * min(heights[left], heights[right])
            max_height = max(max_height, curr_height)
            if heights[left] < heights[right]: 
                left += 1
            elif heights[right] < heights[left]: 
                right -= 1
            else: 
                right -= 1
        
        return max_height
        