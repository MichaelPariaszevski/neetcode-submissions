# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None: 
            return False
        elif root.left is None and root.right is None: 
            return True if root.val == 1 else False

        left_result: bool = self.evaluateTree(root.left)
        right_result: bool = self.evaluateTree(root.right)

        if root.val == 2: 
            return left_result or right_result
        else: 
            return left_result and right_result

        
        