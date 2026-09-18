# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSThelper(root, -1000000000, 1000000000)

    def isValidBSThelper(self, root: Optional[TreeNode], low: int, high: int) -> bool: 
        if root is None: 
            return True

        if root.val <= low or root.val >= high: 
            return False 

        left = self.isValidBSThelper(root.left, low, root.val)
        right = self.isValidBSThelper(root.right, root.val, high)

        return left and right

        

        