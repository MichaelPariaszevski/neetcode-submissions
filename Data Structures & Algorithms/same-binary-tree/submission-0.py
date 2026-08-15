# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True

        def dfs(p, q): 
            if (p and q and p.val != q.val) or (not p and q) or (not q and p): 
                self.same = False
                return 

            if p is None and q is None: 
                return 

            dfs(p.left, q.left)
            dfs(p.right, q.right)

            return 

        dfs(p, q)
        return self.same
        