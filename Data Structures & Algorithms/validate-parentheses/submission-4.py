class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s: 
            if char in char_map: 
                if stack and stack[-1] == char_map[char]: 
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(char)

        return False if stack else True