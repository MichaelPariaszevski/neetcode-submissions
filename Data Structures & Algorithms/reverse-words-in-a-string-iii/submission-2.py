class Solution:
    def reverseWords(self, s: str) -> str:
        result_str: str = ""

        left, right = 0, 0

        while left < len(s): 
            if s[right] == " ": 
                while right < len(s) and s[right] == " ": 
                    right += 1
                result_str += s[left : right]
                left = right
            else: 
                while right < len(s) and s[right] != " ": 
                    right += 1
                result_str += s[left : right][::-1]
                left = right

        return result_str

