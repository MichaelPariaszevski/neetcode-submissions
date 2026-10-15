class Solution:
    def __init__(self): 
        self.s: str
        self.word_set: Set[str]
        self.word_set_lens: Set[int]
        self.memo: List[int, bool] = {}
        self.result: bool = False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.word_set = set(wordDict)
        self.word_set_lens = set([len(word) for word in self.word_set])

        self.dfs(0)

        return self.result
        
    def dfs(self, index: int): 
        if index == len(self.s): 
            self.result = True
            return
        elif index in self.memo: 
            return self.memo[index]

        curr_level: Set[bool] = set()

        for length in self.word_set_lens: 
            if self.s[index : index + length] in self.word_set: 
                curr_res = self.dfs(index + length)
                curr_level.add(curr_res)
                
        self.memo[index] = True if True in curr_level else False
            
        return False

        