# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: 
            return root
            
        queue = [root]

        while queue: 
            node = queue.pop(0)
            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left is not None: 
                queue.append(node.left)

            if node.right is not None: 
                queue.append(node.right)

        return root

