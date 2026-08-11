class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1: 
            return True

        s = s.lower()

        head, tail = 0, len(s) - 1

        while head < tail: 
            if not is_alpha_num(s[head]): 
                head += 1
                continue
            if not is_alpha_num(s[tail]): 
                tail -= 1
                continue

            if s[head] != s[tail]: 
                return False
            else: 
                head += 1
                tail -= 1

        return True

def is_alpha_num(char: str): 
    if ord("A") <= ord(char) <= ord("Z") or ord("a") <= ord(char) <= ord("z") or ord("0") <= ord(char) <= ord("9"): 
        return True 
    else: 
        return False