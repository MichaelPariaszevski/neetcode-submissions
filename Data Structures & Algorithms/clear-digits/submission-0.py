class Solution:
    def clearDigits(self, s: str) -> str:
        stack: List[str] = []
        for char in s: 
            if ord(char) >= 97 and ord(char) <= 122: 
                stack.append(char)
            else: 
                stack.pop(-1)

        return "".join(stack)
