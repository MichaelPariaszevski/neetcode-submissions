class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: 
            return len(s)

        hash_map = {}

        left, right = 0, 1

        hash_map[s[left]] = 1
        max_count = 0

        while right < len(s): 
            if s[right] in hash_map:
                hash_map.pop(s[left]) 
                left += 1
            else: 
                hash_map[s[right]] = 1
                right += 1
                max_count = max(right - left, max_count)

        return max_count
