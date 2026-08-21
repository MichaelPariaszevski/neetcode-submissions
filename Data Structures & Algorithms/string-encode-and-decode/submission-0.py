class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""

        for string in strs: 
            final_str += str(len(string)) + "#" + string

        return final_str

        # 5#Hello5#World

    def decode(self, s: str) -> List[str]:
        index = 0
        curr_len_string = ""
        list_of_strings = []

        while index < len(s): 
            while s[index] != "#": 
                curr_len_string += s[index]
                index += 1
            index += 1

            len_string = int(curr_len_string)

            curr_string = ""

            for i in range(len_string):
                curr_string += s[index]
                index += 1

            list_of_strings.append(curr_string)

            curr_len_string = ""

        return list_of_strings
