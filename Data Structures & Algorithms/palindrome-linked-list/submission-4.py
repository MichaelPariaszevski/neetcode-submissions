# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next: 
            return True 

        slow, fast = head, head

        stack_even: List[int] = []
        stack_odd: List[int] = []

        while fast and fast.next: 
            stack_even.append(slow.val)
            stack_odd.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        slow_even = slow
        slow_odd = slow.next

        while slow_even: 
            if len(stack_even) > 0 and stack_even[-1] == slow_even.val: 
                stack_even.pop(-1)
            else:
                stack_even.append(slow_even.val)
            slow_even = slow_even.next

        while slow_odd: 
            if len(stack_odd) > 0 and stack_odd[-1] == slow_odd.val: 
                stack_odd.pop(-1)
            else: 
                stack_odd.append(slow_odd.val)
            slow_odd = slow_odd.next

        return True if len(stack_even) == 0 or len(stack_odd) == 0 else False

        
            

        

        