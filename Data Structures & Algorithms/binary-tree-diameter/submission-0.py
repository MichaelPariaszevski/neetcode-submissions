# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(root: Optional[TreeNode]) -> int: 
            nonlocal max_diameter

            if root is None: 
                return -1

            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right) 

            max_diameter = max(left + right, max_diameter)

            return max(right, left)

        dfs(root)

        return max_diameter




        