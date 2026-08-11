class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {
            "}": "{", 
            "]": "[", 
            ")": "(",
        }

        for char in s: 
            corresponding_char = char_map.get(char, "")
            if len(stack) == 0 or corresponding_char != stack[-1]: 
                stack.append(char)
            else: 
                stack.pop()

        if len(stack) == 0: 
            return True
        else: 
            return False

        