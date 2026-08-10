class ListNode: 
    def __init__(self, val: int, next: ListNode | None = None): 
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        head = self.head.next
        counter = 0

        while head is not None: 
            if counter == index: 
                return head.val
            head = head.next
            counter += 1

        return -1


    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node
        if not new_node.next: 
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val, None)
        self.tail.next = new_node
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        # head = self.head

        # for i in range(index): 
        #     head = head.next
        #     if head is None: 
        #         return False
            
        # head.next = head.next.next
        
        # return True

        head = self.head
        counter = 0

        while head is not None and head.next is not None: 
            if counter == index: 
                if not head.next.next: 
                    self.tail = head
                    head.next = None
                else: 
                    head.next = head.next.next
                return True
            head = head.next
            counter += 1

        return False

    def getValues(self) -> List[int]:
        head = self.head.next
        values = []

        while head is not None: 
            values.append(head.val)
            head = head.next

        return values
        
