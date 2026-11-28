# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        flattened: List[int] = self.dfs(root)

        min_distance: int = 100000

        for i in range(len(flattened) - 1):
            min_distance = min(min_distance, flattened[i + 1] - flattened[i])

        return min_distance

    def dfs(self, root: Optional[TreeNode]) -> List[int]: 
        if root is None: 
            return []
        elif root.left is None and root.right is None: 
            return [root.val]

        left_result = self.dfs(root.left)
        right_result = self.dfs(root.right)

        return left_result + [root.val] + right_result
        