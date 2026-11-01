class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index_to_insert = 0

        left, right = 0, len(intervals) - 1

        while left <= right: 
            mid = (left + right) // 2
            if intervals[mid][0] == newInterval[0]: 
                left = mid
                break
            elif intervals[mid][0] > newInterval[0]: 
                right = mid - 1
            else: 
                left = mid + 1

        # Returning left means that we always return the index just to the right of the index that we found/"mid" (which is what we want for this problem)
            
        index_to_insert = left

        if index_to_insert > 0 and intervals[index_to_insert - 1][1] >= newInterval[0]: 
            intervals[index_to_insert - 1] = [intervals[index_to_insert - 1][0], max(intervals[index_to_insert - 1][1], newInterval[1])]
            curr_index = index_to_insert - 1
        else: 
            intervals.insert(index_to_insert, newInterval)
            curr_index = index_to_insert

        while curr_index + 1 < len(intervals) and intervals[curr_index][1] >= intervals[curr_index + 1][0]: 
            intervals[curr_index] = [intervals[curr_index][0], max(intervals[curr_index][1], intervals[curr_index + 1][1])]
            intervals.pop(curr_index + 1)

        return intervals
        