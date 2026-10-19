class Solution:
    def __init__(self): 
        self.memo: Dict[tuple[int, int], int] = {}
        self.result: int = 0
        self.text1: str
        self.text2: str

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1 = text1
        self.text2 = text2

        for index in range(len(text1)): 
            dfs_result = self.dfs(index, 0)
            self.result = max(self.result, dfs_result)

        return self.result

    def dfs(self, text_1_index: int, text_2_index: int):
        if text_1_index >= len(self.text1) or text_2_index >= len(self.text2): 
            return 0 
        if (text_1_index, text_2_index) in self.memo: 
            return self.memo[(text_1_index, text_2_index)]
        elif self.text1[text_1_index] == self.text2[text_2_index]:
            curr_result = 1 + self.dfs(text_1_index + 1, text_2_index + 1)  
            self.memo[(text_1_index, text_2_index)] = curr_result
            return curr_result
        else: 
            curr_result_1 = self.dfs(text_1_index, text_2_index + 1)
            curr_result_2 = self.dfs(text_1_index + 1, text_2_index)
            max_result = max(curr_result_1, curr_result_2)
            self.memo[(text_1_index, text_2_index)] = max_result
            return max_result

        