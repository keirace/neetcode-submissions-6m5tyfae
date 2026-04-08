class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # return how many intervals to remove
        count = 0
        intervals.sort()
        # keeping track of the last valid end
        prevend = intervals[0][1]
        for i in range(1, len(intervals)):
            # overlapped: new start < prev end
            if intervals[i][0] < prevend:
                count += 1
                prevend = min(intervals[i][1], prevend)
            else:
                prevend = intervals[i][1]

        return count