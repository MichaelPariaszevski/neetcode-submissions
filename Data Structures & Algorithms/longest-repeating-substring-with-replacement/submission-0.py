class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}
        max_frequency = 0
        max_length = 0

        left = 0

        for right in range(len(s)): 
            char_map[s[right]] = char_map.get(s[right], 0) + 1
            max_frequency = max(max_frequency, char_map[s[right]])
            while (right - left + 1) - max_frequency > k: 
                char_map[s[left]] = char_map.get(s[left]) - 1
                left += 1
                max_frequency = max(char_map.values())
            max_length = max(max_length, right - left + 1)

        return max_length