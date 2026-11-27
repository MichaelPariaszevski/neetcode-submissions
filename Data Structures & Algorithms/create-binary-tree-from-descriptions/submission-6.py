# class TreeNode: 
#     def __init__(self, val: int, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None): 
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hash_map: Dict[int, TreeNode] = {}
        possible_heads: Set[TreeNode] = set()

        for parent, child, isLeft in descriptions: 
            if parent not in hash_map and child not in hash_map: 
                parent_node = TreeNode(parent, None, None)
                child_node = TreeNode(child, None, None)

                if isLeft == 1: 
                    parent_node.left = child_node
                else: 
                    parent_node.right = child_node

                hash_map[parent] = parent_node
                hash_map[child] = child_node
                possible_heads.add(parent_node)
            elif parent in hash_map:
                if child in hash_map and hash_map[child] in possible_heads: 
                    possible_heads.remove(hash_map[child])

                child_node = hash_map[child] if child in hash_map else TreeNode(child, None, None)

                if isLeft == 1: 
                    hash_map[parent].left = child_node
                else: 
                    hash_map[parent].right = child_node

                if child not in hash_map: 
                    hash_map[child] = child_node
            elif child in hash_map: 
                if hash_map[child] in possible_heads: 
                    possible_heads.remove(hash_map[child])
                
                parent_node = hash_map[parent] if parent in hash_map else TreeNode(parent, None, None)

                if isLeft == 1: 
                    parent_node.left = hash_map[child]
                else:
                    parent_node.right = hash_map[child]

                if parent not in hash_map: 
                    possible_heads.add(parent_node)
                    hash_map[parent] = parent_node

        return possible_heads.pop() if len(possible_heads) == 1 else None

                




