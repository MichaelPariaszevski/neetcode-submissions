class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest_string = ""
        t_map = {}
        s_map = {}

        for char in t: 
            t_map[char] = t_map.get(char, 0) + 1

        matched_count = 0
        left = 0
        len_t_map = len(t_map)

        for right in range(len(s)): 
            s_map[s[right]] = s_map.get(s[right], 0) + 1
            if s[right] in t_map and s_map[s[right]] == t_map[s[right]]: 
                matched_count += 1
                while matched_count == len_t_map: 
                    if s[left] not in t_map:
                        left += 1
                        continue
                    s_map[s[left]] = s_map[s[left]] - 1
                    if s_map[s[left]] == t_map[s[left]] - 1: 
                        shortest_string = s[left:right + 1] if (not shortest_string or len(s[left:right + 1]) < len(shortest_string)) else shortest_string
                        matched_count -= 1
                    left += 1

        return shortest_string

