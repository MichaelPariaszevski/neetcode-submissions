# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self): 
        self.max = -1001

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSumHelper(root)

        return self.max

    def maxPathSumHelper(self, root: Optional[TreeNode]) -> int: 
        if root is None: 
            return -1001

        left_max = self.maxPathSumHelper(root.left)
        right_max = self.maxPathSumHelper(root.right)

        curr_max = max(root.val, root.val + left_max, root.val + right_max, root.val + left_max + right_max)

        if curr_max > self.max: 
            self.max = curr_max

        if curr_max == root.val + left_max + right_max: 
            curr_max = max(root.val, root.val + left_max, root.val + right_max)

        return curr_max


        