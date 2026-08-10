class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
            
        string_map_1 = {}
        string_map_2 = {}

        for i in range(len(s)): 
            string_map_1[s[i]] = string_map_1.get(s[i], 0) + 1
            string_map_2[t[i]] = string_map_2.get(t[i], 0) + 1

        if string_map_1 == string_map_2: 
            return True
        else: 
            return False