class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word_1, len_word_2 = len(word1), len(word2)
        max_len = max(len_word_1, len_word_2)
        new_str_arr: list = []

        for i in range(max_len): 
            if i < len_word_1: 
                new_str_arr.append(word1[i])

            if i < len_word_2: 
                new_str_arr.append(word2[i])

        return "".join(new_str_arr)