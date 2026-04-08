class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            new_start, new_end = newInterval
            res_start = start
            # new interval ends before, won't overlap
            if new_end < start:
                res.append(newInterval)
                return res + intervals[i:] # add the rest
            # new interval starts after, won't overlap
            elif new_start > end:
                res.append(intervals[i])
            # overlapped, adjust the start end end of the new interval
            else:
                newInterval = [min(start, new_start), max(end, new_end)]
        res.append(newInterval)
        return res