# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        full_arr = []

        for l in lists: 
            curr = l
            while curr is not None: 
                full_arr.append(curr.val)
                curr = curr.next

        if not full_arr: 
            return 

        full_arr.sort()

        head = ListNode(full_arr[0], None)
        curr = head

        for i in range(1, len(full_arr)): 
            curr.next = ListNode(full_arr[i], None)
            curr = curr.next

        return head
        