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

        queue = [root]

        max_depth = 0

        while queue: 
            for _ in range(len(queue)): 
                current = queue.pop(0)
                if current.left: 
                    queue.append(current.left)

                if current.right: 
                    queue.append(current.right)

            max_depth += 1

        return max_depth
