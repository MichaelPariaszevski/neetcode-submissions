# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        stack = [[root, 1]]

        max_depth = 1

        while stack: 
            current, depth = stack.pop()

            if current.left: 
                stack.append([current.left, depth + 1])

            if current.right: 
                stack.append([current.right, depth + 1])

            max_depth = max(depth, max_depth)

        return max_depth
