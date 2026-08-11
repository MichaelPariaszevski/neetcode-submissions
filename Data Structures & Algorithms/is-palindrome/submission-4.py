class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.replace(" ", "").replace("?", "").replace(".", "").replace(",", "").replace("'", "").replace(":", "").replace("!", "").lower()

        for i in range(len(new_s)): 
            if new_s[i] != new_s[-1 * (i + 1)]: 
                return False
        
        return True
        