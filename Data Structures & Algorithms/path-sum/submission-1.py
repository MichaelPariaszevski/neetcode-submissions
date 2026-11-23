# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, 0, targetSum)

    def dfs(self, root: Optional[TreeNode], curr_val: int, targetSum: int): 
        if root is None: 
            return False
        elif root.left is None and root.right is None: 
            if curr_val + root.val == targetSum: 
                return True
            else: 
                return False

        left_result: bool = self.dfs(root.left, curr_val + root.val, targetSum)
        right_result: bool = self.dfs(root.right, curr_val + root.val, targetSum)

        return left_result or right_result



        
        