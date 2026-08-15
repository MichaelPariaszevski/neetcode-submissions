# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #dfs, if height difference between any two paths (at any node) is greater than or equal to two, return false
        self.balanced = True

        def dfs(root): 
            if root is None: 
                return 0 

            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right) 

            if abs(right - left) >= 2: 
                self.balanced = False

            return max(left, right)

        dfs(root)
        return self.balanced

        
        