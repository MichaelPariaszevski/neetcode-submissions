class Solution:
    def minLength(self, s: str) -> int:
        stack: List[s] = []

        for char in s: 
            if len(stack) == 0: 
                stack.append(char)
            elif (stack[-1] == "A" and char == "B") or (stack[-1] == "C" and char == "D"): 
                stack.pop(-1)
            else: 
                stack.append(char)

        return len(stack)
            
