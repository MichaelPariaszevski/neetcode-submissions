# class TreeNode: 
#     def __init__(self, val, left = None, right = None): 
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums or len(nums) == 0: 
            return None
        elif len(nums) == 1: 
            return TreeNode(nums[0], None, None)

        mid = len(nums) // 2
        root = TreeNode(nums[mid], None, None)

        root.left: Optional[TreeNode] = self.sortedArrayToBST(nums[0:mid])
        root.right: Optional[TreeNode] = self.sortedArrayToBST(nums[mid + 1:] if mid + 1 < len(nums) else [])

        return root
