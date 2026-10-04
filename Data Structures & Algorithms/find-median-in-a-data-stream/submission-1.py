class MedianFinder:

    def __init__(self):
        self.lower_half_max_heap = []
        self.upper_half_min_heap = []
        # self.upper_len: int = 0
        # self.lower_len: int = 0
        
    def addNum(self, num: int) -> None:
        if len(self.lower_half_max_heap) == 0 and len(self.upper_half_min_heap) == 0: 
            heapq.heappush(self.lower_half_max_heap, -num)
        elif num > -self.lower_half_max_heap[0]: 
            heapq.heappush(self.upper_half_min_heap, num)
        else: 
            heapq.heappush(self.lower_half_max_heap, -num)

        upper_len = len(self.upper_half_min_heap)
        lower_len = len(self.lower_half_max_heap)

        if abs(upper_len - lower_len) > 1: 
            if lower_len > upper_len: 
                heapq.heappush(self.upper_half_min_heap, -heapq.heappop(self.lower_half_max_heap))
            else: 
                heapq.heappush(self.lower_half_max_heap, -heapq.heappop(self.upper_half_min_heap)) 

    def findMedian(self) -> float:
        upper_len = len(self.upper_half_min_heap)
        lower_len = len(self.lower_half_max_heap)

        if upper_len != lower_len: 
            if lower_len > upper_len: 
                return -self.lower_half_max_heap[0]
            else: 
                return self.upper_half_min_heap[0]

        return (-self.lower_half_max_heap[0] + self.upper_half_min_heap[0]) / 2
        
        