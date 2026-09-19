# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self): 
        self.count = 0
        self.value = -1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kthSmallestHelper(root, k)
        return self.value
        
    def kthSmallestHelper(self, root: Optional[TreeNode], k: int) -> int: 
        if root is None: 
            return

        left = self.kthSmallestHelper(root.left, k)

        self.count += 1

        if self.count == k: 
            self.value = root.val

        right = self.kthSmallestHelper(root.right, k)
        