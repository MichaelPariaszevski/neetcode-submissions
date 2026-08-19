class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = {}

        for string in strs: 
            base_arr = [0] * 26
            for i in range(len(string)): 
                index = ord(string[i]) - ord('a')
                base_arr[index] += 1

            str_tuple = tuple(base_arr)
            group_map.setdefault(str_tuple, []).append(string)

        final_arr = []

        for result in group_map.values(): 
            final_arr.append(result)

        return final_arr
            