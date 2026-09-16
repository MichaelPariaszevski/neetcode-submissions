# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return [] 

        tree_list = []

        queue = [root]

        while len(queue) > 0: 
            amount_to_pop = len(queue)
            current_level = []
            for _ in range(amount_to_pop): 
                node_popped = queue.pop(0)
                current_level.append(node_popped.val)
                if node_popped.left is not None: 
                    queue.append(node_popped.left)
                if node_popped.right is not None:
                    queue.append(node_popped.right)
            tree_list.append(current_level)

        return tree_list

        