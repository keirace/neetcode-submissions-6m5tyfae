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
        
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        e = 0
        rooms = 0
        for s in range(len(starts)):
            # a meeting starts before the eatliest one ended
            if starts[s] < ends[e]:
                rooms += 1
            else: # a meeting ended
                e += 1

        return rooms