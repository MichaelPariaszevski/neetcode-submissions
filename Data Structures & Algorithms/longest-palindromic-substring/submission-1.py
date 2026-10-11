class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        for index in range(len(s)): 
            left = index 
            right = index
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if (right - 1) - (left + 1) + 1 > len(result): 
                result = s[left + 1 : right]

            left = index
            right = index + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if (right - 1) - (left + 1) + 1 > len(result): 
                result = s[left + 1 : right]


        return result


        