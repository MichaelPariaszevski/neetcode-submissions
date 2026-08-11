# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return 

        if head.next is None: 
            return head

        prev = None
        curr = head
        temp = head.next

        while temp is not None: 
            curr.next = prev
            prev = curr
            curr = temp
            temp = temp.next

        curr.next = prev

        return curr
        