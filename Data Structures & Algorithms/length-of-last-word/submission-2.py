class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1: 
            return 1
            
        left, right = len(s) - 1, len(s) - 1
        while s[right] == " ": 
            right -= 1

        left = right 

        while s[left] != " ": 
            left -= 1

        return right - left
        