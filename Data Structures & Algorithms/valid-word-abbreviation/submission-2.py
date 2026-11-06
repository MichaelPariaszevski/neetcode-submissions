class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr: int = 0
        abbr_ptr: int = 0

        while word_ptr < len(word) and abbr_ptr < len(abbr): 
            if abbr[abbr_ptr].isdecimal(): 
                curr_num_arr: List[int] = []

                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdecimal(): 
                    curr_num_arr.append(abbr[abbr_ptr])
                    abbr_ptr += 1

                if curr_num_arr[0] == "0": 
                    return False

                curr_num = int("".join(curr_num_arr))

                word_ptr += curr_num
            else: 
                if word[word_ptr] != abbr[abbr_ptr]: 
                    return False
                
                word_ptr += 1
                abbr_ptr += 1

        return True if word_ptr == len(word) and abbr_ptr == len(abbr) else False

        