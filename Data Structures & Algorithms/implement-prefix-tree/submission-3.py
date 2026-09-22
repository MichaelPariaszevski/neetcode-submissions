class Node: 
    def __init__(self): 
        self.children: list[str, Node | bool] = {}

class PrefixTree:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        curr_level = self.root
        for char in word: 
            if char not in curr_level.children: 
                curr_level.children[char] = Node()
            curr_level = curr_level.children[char]
        curr_level.children["*"] = True
            
    def search(self, word: str) -> bool:
        curr_level = self.root
        for char in word: 
            if char not in curr_level.children: 
                return False
            curr_level = curr_level.children[char]

        if "*" not in curr_level.children: 
            return False
        
        return True
        

    def startsWith(self, prefix: str) -> bool:
        curr_level = self.root
        for char in prefix: 
            if char not in curr_level.children: 
                return False 
            curr_level = curr_level.children[char]

        return True
        
        