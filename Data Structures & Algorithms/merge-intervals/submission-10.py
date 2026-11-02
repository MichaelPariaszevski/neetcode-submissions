class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])

        curr_index = 0

        while curr_index + 1 < len(intervals): 
            stop = False

            while intervals[curr_index][1] < intervals[curr_index + 1][0]: 
                curr_index += 1
                if curr_index + 1 >= len(intervals): 
                    stop = True
                    break

            if stop: 
                break

            intervals[curr_index] = [intervals[curr_index][0], max(intervals[curr_index][1], intervals[curr_index + 1][1])]
            intervals.pop(curr_index + 1)

        return intervals


        


        