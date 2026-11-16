# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = ListNode(0, head)

        prev, curr = new_head, new_head.next

        while curr: 
            if curr.val == val: 
                prev.next = curr.next
                curr.next = None
                curr = prev.next
            else: 
                prev = curr
                curr = curr.next

        return new_head.next
        