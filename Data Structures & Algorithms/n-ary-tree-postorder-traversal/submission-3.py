"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None: 
            return []
        elif root.children is None or len(root.children) == 0: 
            return [root.val]

        child_arr = []

        for child in root.children: 
            child_arr += self.postorder(child)

        return child_arr + [root.val]
        