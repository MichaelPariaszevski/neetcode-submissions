class Solution:
    def clearDigits(self, s: str) -> str:
        dq: List[str] = deque([])
        for char in s: 
            if ord(char) >= 97 and ord(char) <= 122: 
                dq.append(char)
            else: 
                dq.pop()

        return "".join(dq)
