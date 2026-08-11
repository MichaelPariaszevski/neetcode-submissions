# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        new_head = new_list

        while list1 is not None or list2 is not None: 
            if list1 and (not list2 or list1.val <= list2.val): 
                new_head.next = list1
                new_head = new_head.next
                list1 = list1.next
            else: 
                new_head.next = list2
                new_head = new_head.next
                list2 = list2.next

        return new_list.next




        