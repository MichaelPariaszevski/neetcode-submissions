# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        counter = 0

        for l in lists:
            if l is not None: 
                heapq.heappush(min_heap, (l.val, counter, l))
                counter += 1

        head = ListNode(0, None)
        curr = head

        while len(min_heap) > 0: 
            (val, counter, node) = heapq.heappop(min_heap)
            curr.next = ListNode(val, None)
            curr = curr.next
            node_to_push = node.next
            if node_to_push is not None: 
                heapq.heappush(min_heap, (node_to_push.val, counter, node_to_push))
                counter += 1

        return head.next