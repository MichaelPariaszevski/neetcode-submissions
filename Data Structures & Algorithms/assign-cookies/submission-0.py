class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result: int = 0
        visited_indexes: Set[int] = set()

        for i in range(len(g)): 
            curr_min: int = -1
            curr_index: int = -1
            for j in range(len(s)): 
                if s[j] >= g[i] and j not in visited_indexes and (s[j] < curr_min or curr_min == -1): 
                    curr_min = s[j]
                    curr_index = j

            if curr_min != -1: 
                visited_indexes.add(curr_index)
                result += 1

        return result
        