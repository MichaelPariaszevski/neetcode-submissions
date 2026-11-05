class Solution:
    def makeGood(self, s: str) -> str:
        stack: List[str] = []
        for char in s: 
            if len(stack) > 0 and stack[-1].lower() == char.lower() and stack[-1] != char: 
                stack.pop(-1)
            else: 
                stack.append(char)

        return "".join(stack)
