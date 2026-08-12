# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast is not None: 
            if slow.next is not None: 
                slow = slow.next
            else: 
                return False

            if fast.next is not None and fast.next.next is not None: 
                fast = fast.next.next
            else: 
                return False

            if slow.val == fast.val: 
                return True

        return False
