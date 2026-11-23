# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: 
            return []

        left_result: List[int] = self.inorderTraversal(root.left)
        right_result: List[int] = self.inorderTraversal(root.right)

        return left_result + [root.val] + right_result