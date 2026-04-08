"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 2 pointers
        if not intervals:
            return 0
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        i, j = 0, 0
        count = 0 # number of rooms at a specific time
        res = 0 # total min num of rooms needed
        n = len(intervals)
        while i < n:
            if start[i] < end[j]: # conflict; add room
                count += 1
                i += 1
                res = max(res, count)
            else:
                j += 1
                count -= 1 # room is free
        
        return res