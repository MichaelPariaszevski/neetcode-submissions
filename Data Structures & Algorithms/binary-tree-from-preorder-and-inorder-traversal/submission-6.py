# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self): 
        self.inorder_hash_map: Dict[int, int] = {}
        self.preorder: List[int] = []

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i, val in enumerate(inorder): 
            self.inorder_hash_map[val] = i

        self.preorder = preorder

        return self.buildTreeHelper(0, len(inorder) - 1, 0, len(preorder) - 1)


    def buildTreeHelper(self, in_start: int, in_end: int, pre_start: int, pre_end: int) -> Optional[TreeNode]: 
        if in_start > in_end or pre_start > pre_end: 
            return None

        root_val = self.preorder[pre_start]

        root = TreeNode(root_val, None, None)

        inorder_root_index = self.inorder_hash_map[root_val]

        new_in_start_left = in_start
        new_in_end_left = inorder_root_index - 1
        new_in_start_right = inorder_root_index + 1
        new_in_end_right = in_end

        len_inorder_left_subtree = (new_in_end_left - new_in_start_left) + 1
        len_inorder_right_subtree = (new_in_end_right - new_in_start_right) + 1

        new_pre_start_left = pre_start + 1
        new_pre_end_left = new_pre_start_left + len_inorder_left_subtree
        new_pre_start_right = new_pre_end_left
        new_pre_end_right = new_pre_start_right + len_inorder_right_subtree

        root.left = self.buildTreeHelper(new_in_start_left, new_in_end_left, new_pre_start_left, new_pre_end_left)
        root.right = self.buildTreeHelper(new_in_start_right, new_in_end_right, new_pre_start_right, new_pre_end_right)

        return root


