class Node: 
    def __init__(self, val: int = 0, next: Node | None = None, prev: Node | None = None): 
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = self.head
        

    def get(self, index: int) -> int:
        curr = self.head

        for i in range(index): 
            curr = curr.next
            if curr is None: 
                return -1

        return curr.val
        

    def addAtHead(self, val: int) -> None:
        if not self.head and not self.tail: 
            self.head = Node(val, None, None)
            self.tail = self.head
        else: 
            temp = self.head 
            self.head = Node(val, temp, None)
            temp.prev = self.head

        return
        
    def addAtTail(self, val: int) -> None:
        if not self.tail and not self.head: 
            self.addAtHead(val)
        else:
            temp = self.tail
            self.tail = Node(val, None, temp)
            temp.next = self.tail

        return 

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0: 
            self.addAtHead(val)

        curr = self.head

        for i in range(index - 1):
            if curr is None: 
                return
            curr = curr.next

        if curr.next is None: 
            self.addAtTail(val)
        else:
            new_node = Node(val, curr.next, curr)
            curr.next.prev = new_node
            curr.next = new_node

        return

    def deleteAtIndex(self, index: int) -> None:
        if not self.head and not self.tail: 
            return 

        if index == 0: 
            self.head = self.head.next
            if not self.head: 
                self.tail = None
            else:
                self.head.prev = None
            return

        curr = self.head

        for i in range(index):
            curr = curr.next
            if not curr: 
                return

        if curr.next is None: 
            curr.prev.next = None
            self.tail = self.tail.prev
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.next = None
            curr.prev = None

        return 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)