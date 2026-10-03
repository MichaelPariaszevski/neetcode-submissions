class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list: Dict[int, List[int]] = {}

        for starting_node, neighbor in edges: 
            if starting_node not in adjacency_list: 
                adjacency_list[starting_node] = []
            adjacency_list[starting_node].append(neighbor)

            if neighbor not in adjacency_list: 
                adjacency_list[neighbor] = []
            adjacency_list[neighbor].append(starting_node)

        num_islands = 0
        visited: Set[int] = set()

        for node in range(n): 
            if node in visited or node not in adjacency_list: 
                continue 

            num_islands += 1
            queue = deque([node])

            while len(queue) > 0: 
                curr_node = queue.popleft()
                visited.add(curr_node)

                for neighbor in adjacency_list[curr_node]: 
                    if neighbor not in visited: 
                        queue.append(neighbor)

        return num_islands + n - len(visited)