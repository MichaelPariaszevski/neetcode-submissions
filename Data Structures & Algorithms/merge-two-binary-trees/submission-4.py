# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root1, root2)

    def dfs(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]: 
        if root1 is None and root2 is None: 
            return None

        if root1 is None: 
            new_node_val = root2.val
        elif root2 is None: 
            new_node_val = root1.val
        else: 
            new_node_val = root1.val + root2.val

        root1_left = root1.left if root1 is not None else None
        root1_right = root1.right if root1 is not None else None
        root2_left = root2.left if root2 is not None else None
        root2_right = root2.right if root2 is not None else None

        result_left: Optional[TreeNode] = self.dfs(root1_left, root2_left)
        result_right: Optional[TreeNode] = self.dfs(root1_right, root2_right)

        return TreeNode(new_node_val, result_left, result_right)


        