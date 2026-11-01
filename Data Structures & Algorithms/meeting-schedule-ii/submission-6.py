"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key = lambda interval: interval.start)

        min_heap_of_ends = [intervals[0].end]
        
        heapq.heapify(min_heap_of_ends)

        num_rooms = 1

        for i in range(1, len(intervals)): 
            if intervals[i].start < min_heap_of_ends[0]: 
                num_rooms += 1
            else: 
                heapq.heappop(min_heap_of_ends)
            heapq.heappush(min_heap_of_ends, intervals[i].end)

        return num_rooms

    



        