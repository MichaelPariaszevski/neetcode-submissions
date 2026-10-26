class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: 
            return True
            
        s_index = 0
        s_len = len(s)

        for i in range(len(t)): 
            if t[i] == s[s_index]: 
                s_index += 1
                if s_index == s_len: 
                    return True 

        return False
        