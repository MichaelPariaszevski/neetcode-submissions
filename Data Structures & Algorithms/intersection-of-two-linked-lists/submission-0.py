# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_set: Set[ListNode] = set()

        curr_a = headA

        while curr_a: 
            hash_set.add(curr_a)
            curr_a = curr_a.next

        curr_b = headB

        while curr_b: 
            if curr_b in hash_set: 
                return curr_b
            curr_b = curr_b.next

        return None