class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: 
            return False

        if len(edges) == 0 and n == 1: 
            return True

        adjacency_list: Dict[int, List[int]] = {}

        for first_node, second_node in edges: 
            if first_node not in adjacency_list: 
                adjacency_list[first_node] = []
            adjacency_list[first_node].append(second_node)

            if second_node not in adjacency_list: 
                adjacency_list[second_node] = []
            adjacency_list[second_node].append(first_node)

        visited: set[int] = set()

        num_visited = 0

        queue = deque([0])

        while len(queue) > 0: 
            curr_node = queue.popleft()
            if curr_node not in visited: 
                visited.add(curr_node)
                num_visited += 1
                for node in adjacency_list[curr_node]: 
                    queue.append(node)

        return True if num_visited == n else False
            

        