class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack: List[str] = []
        t_stack: List[str] = []

        for char in s: 
            if char == "#": 
                if len(s_stack) > 0: 
                    s_stack.pop(-1)
            else: 
                s_stack.append(char)

        for char in t: 
            if char == "#": 
                if len(t_stack) > 0: 
                    t_stack.pop(-1)
            else: 
                t_stack.append(char)

        return True if s_stack == t_stack else False

            
