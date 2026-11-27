# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: 
            return []
        elif root.left is None and root.right is None: 
            return [root.val]

        result_left = self.postorderTraversal(root.left)
        result_right = self.postorderTraversal(root.right)

        return result_left + result_right + [root.val]