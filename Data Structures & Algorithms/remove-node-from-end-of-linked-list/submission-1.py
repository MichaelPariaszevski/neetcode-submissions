# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None: 
            return 

        return_head = head
        slow, fast = head, head

        for i in range(n):
            fast = fast.next

        if fast is None: 
            return head.next

        while fast.next is not None: 
            slow = slow.next
            fast = fast.next 
  
        temp = slow.next.next
        slow.next.next = None
        slow.next = temp


        return return_head
        

        
