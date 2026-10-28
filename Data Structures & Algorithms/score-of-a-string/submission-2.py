class Solution:
    def scoreOfString(self, s: str) -> int:
        left, right = 0, 1
        result = 0
        while right < len(s): 
            result += abs(ord(s[right]) - ord(s[left]))
            left += 1
            right += 1

        return result
        