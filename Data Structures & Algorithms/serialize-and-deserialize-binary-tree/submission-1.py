# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: 
            return ""

        result_arr = []

        dq = deque([root])

        while len(dq) > 0: 
            node = dq.popleft()
            if node is not None: 
                result_arr.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)
            else: 
                result_arr.append("None")

        return "#".join(result_arr)

        # 1#2#3#None#None#4#5#None#None#None#None
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: 
            return 

        serialized = deque(data.split("#"))
        root = TreeNode(int(serialized.popleft()), None, None)
        dq = deque([root])

        while len(dq) > 0: 
            node = dq.popleft()
            left = serialized.popleft()
            right = serialized.popleft()
            left_value = None if left == "None" else int(left)
            right_value = None if right == "None" else int(right)
            if left_value != None: 
                left_tree_node = TreeNode(left_value, None, None)
                dq.append(left_tree_node)
                node.left = left_tree_node
            if right_value != None:
                right_tree_node = TreeNode(right_value, None, None)
                dq.append(right_tree_node)
                node.right = right_tree_node

        return root