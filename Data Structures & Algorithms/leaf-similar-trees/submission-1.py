# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self): 
        self.left_tree_leaves: List[int] = []
        self.right_tree_leaves: List[int] = []

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.dfs(root1, True)
        self.dfs(root2, False)

        return True if self.left_tree_leaves == self.right_tree_leaves else False

    def dfs(self, root: Optional[TreeNode], right_left: bool): 
        if root is None: 
            return
        elif root.left is None and root.right is None: 
            if right_left: 
                self.right_tree_leaves.append(root.val)
                return
            else: 
                self.left_tree_leaves.append(root.val)
                return

        self.dfs(root.left, right_left)
        self.dfs(root.right, right_left)

            

        