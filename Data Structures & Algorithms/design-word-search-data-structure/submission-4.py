class Node: 
    def __init__(self): 
        self.children: list[str, Node | None] = {}

class WordDictionary:
    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        curr_level = self.root 
        for char in word: 
            if char not in curr_level.children: 
                curr_level.children[char] = Node()
            curr_level = curr_level.children[char]
            
        curr_level.children["*"] = True

    def search(self, word: str) -> bool:
        return self.dfs(0, self.root, word)


    def dfs(self, index: int, node: Node, word: str) -> bool: 
        if index == len(word): 
            if "*" in node.children: 
                return True
            else: 
                return False
        
        # found = False

        if word[index] in node.children: 
            return self.dfs(index + 1, node.children[word[index]], word)
        elif word[index] == ".": 
            for new_node in node.children.values(): 
                found = self.dfs(index + 1, new_node, word) if new_node is not True else False
                if found: 
                    return True

        return False

        
        
