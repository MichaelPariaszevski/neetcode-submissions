# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None: 
            return
            
        slow, fast = head, head

        while fast.next is not None and fast.next.next is not None: 
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None
        first_half = head

        prev, curr = None, second_half

        while curr is not None: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        reversed_second_half = prev
        curr = first_half

        while curr is not None and reversed_second_half is not None: 
            temp = curr.next
            curr.next = reversed_second_half
            reversed_second_half = reversed_second_half.next
            curr.next.next = temp
            curr = curr.next.next            


            


        
        