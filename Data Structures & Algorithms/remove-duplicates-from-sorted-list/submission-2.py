# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_set: Set[int] = set()

        new_head = ListNode(-101, head)

        prev, curr = new_head, new_head.next

        while curr: 
            if curr.val in hash_set: 
                prev.next = curr.next
                curr.next = None
                curr = prev.next
            else: 
                hash_set.add(curr.val)
                prev = prev.next
                curr = curr.next

        return new_head.next

            
        