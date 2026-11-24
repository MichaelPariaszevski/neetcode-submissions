# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: 
            return []

        if root.left is None and root.right is None: 
            return [root.val]

        left_result: List[int] = self.preorderTraversal(root.left)
        right_result: List[int] = self.preorderTraversal(root.right)

        return [root.val] + left_result + right_result

        
        