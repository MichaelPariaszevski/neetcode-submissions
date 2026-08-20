class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: 
            return ""

        if len(strs) == 1: 
            return strs[0]

        curr_prefix = ""
        word_index = 0

        while True: 
            curr_char = ""
            for string in strs: 
                if not curr_char: 
                    try: 
                        curr_char = string[word_index]
                        continue
                    except IndexError: 
                        return curr_prefix
                else:
                    try: 
                        if string[word_index] != curr_char: 
                            return curr_prefix
                    except IndexError: 
                        return curr_prefix

            curr_prefix += strs[0][word_index]
            word_index += 1

        return curr_prefix



