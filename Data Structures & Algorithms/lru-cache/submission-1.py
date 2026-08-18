class LRUNode: 
    def __init__(self, key: int, val: int, next: LRUNode | None = None, prev: LRUNode | None = None): 
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hash_map = {}
        self.head = LRUNode(0, 0, None, None)
        self.tail = LRUNode(0, 0, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        node = self.hash_map.get(key, None)
        if node is None: 
            return -1

        val_to_return = node.val


        node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = self.tail.prev.next
        self.hash_map[key] = node

        return val_to_return
        

    def put(self, key: int, value: int) -> None:
        if self.size == self.capacity: 
            node = self.hash_map.get(key, None)
            if node is None: 
                key_to_remove = self.head.next.key
                self.head.next = self.head.next.next
                self.head.next.prev = self.head.next.prev.prev
                new_node = LRUNode(key, value, self.tail, self.tail.prev)
                self.tail.prev.next = new_node
                self.tail.prev = self.tail.prev.next
                self.hash_map[key] = new_node
                self.hash_map.pop(key_to_remove)
            else: 
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.prev.next = node
                node.prev = self.tail.prev
                node.next = self.tail
                self.tail.prev = self.tail.prev.next
                node.val = value
                self.hash_map[key] = node
        elif self.size < self.capacity: 
            node = self.hash_map.get(key, None)
            if node is None: 
                new_node = LRUNode(key, value, self.tail, self.tail.prev)

                self.tail.prev = new_node
                self.tail.prev.prev.next = self.tail.prev
                self.hash_map[key] = new_node
                self.size += 1
            else: 
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.prev.next = node
                node.prev = self.tail.prev
                node.next = self.tail
                self.tail.prev = self.tail.prev.next
                node.val = value
                self.hash_map[key] = node
        else: 
            return ValueError("self.size is greater than self.capacity")
                
        
