"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self): 
        self.clones: dict['Node', 'Node'] = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return 

        return self.dfs(node)

    def dfs(self, node: Optional['Node']): 
        if node in self.clones: 
            return self.clones[node]
        
        self.clones[node] = Node(node.val, None)

        for neighbor in node.neighbors: 
            if neighbor is not None: 
                self.clones[node].neighbors.append(self.dfs(neighbor))

        return self.clones[node]



        
        
        