class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index_to_insert = 0
        while index_to_insert < len(intervals): 
            if intervals[index_to_insert][0] < newInterval[0]: 
                index_to_insert += 1
            else: 
                break

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
        