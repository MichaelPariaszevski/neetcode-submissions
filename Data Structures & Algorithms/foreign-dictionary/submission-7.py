class Solution:
    def __init__(self): 
        self.adj_list: Dict[int, Set[int]] = {}

    def foreignDictionary(self, words: List[str]) -> str:
        in_degree: Dict[str, int] = {}

        for word in words: 
            for char in word: 
                if char not in in_degree: 
                    in_degree[char] = 0

        for i in range(1, len(words)): 
            same_string = False
            inner_index = 0 
            while words[i - 1][inner_index] == words[i][inner_index]: 
                inner_index += 1
                if inner_index >= len(words[i]) and inner_index < len(words[i - 1]): 
                    return ""
                elif inner_index == len(words[i - 1]) and inner_index == len(words[i]) or inner_index >= len(words[i - 1]) and inner_index < len(words[i]): 
                    same_string = True
                    break
            if same_string: 
                continue
            if not self.adj_list.get(words[i - 1][inner_index], None): 
                self.adj_list[words[i - 1][inner_index]] = set()
            if words[i][inner_index] not in self.adj_list[words[i - 1][inner_index]]: 
                self.adj_list[words[i - 1][inner_index]].add(words[i][inner_index])
                in_degree[words[i][inner_index]] = in_degree.get(words[i][inner_index], 0) + 1
        
        queue = deque([])
        result_string = ""

        for char, val in in_degree.items(): 
            if val == 0: 
                queue.append(char)

        while len(queue) > 0: 
            curr_node = queue.popleft()
            result_string += curr_node
            for next_node in self.adj_list.get(curr_node, set()): 
                in_degree[next_node] = in_degree[next_node] - 1
                if in_degree[next_node] == 0:
                    queue.append(next_node)

        return result_string if len(result_string) == len(in_degree) else ""
