# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root_1, root_2): 
            if not root_1 and not root_2: 
                return True
            if not root_1 or not root_2 or root_1.val != root_2.val: 
                return False

            return (isSameTree(root_1.left, root_2.left) and isSameTree(root_1.right, root_2.right))

        same = isSameTree(root, subRoot)

        if same: 
            return True
        elif not root: 
            return False
        else: 
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))