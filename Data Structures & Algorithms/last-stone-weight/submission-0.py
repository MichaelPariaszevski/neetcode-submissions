class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for num in stones: 
            heapq.heappush(max_heap, -num)

        while len(max_heap) > 1: 
            largest = -heapq.heappop(max_heap)
            second_largest = -heapq.heappop(max_heap)
            if largest == second_largest: 
                continue 
            else: 
                heapq.heappush(max_heap, -abs(largest - second_largest))

        return -max_heap[0] if len(max_heap) > 0 else 0
        