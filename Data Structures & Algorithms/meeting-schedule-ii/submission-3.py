"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)

        # get the earliest end
        minheap = [intervals[0].end] # min end
        for i in intervals[1:]:
            start, end = i.start, i.end
            if minheap[0] <= start: # no overlap
                # pop prev min end
                heapq.heappop(minheap)
            # push in current end
            heapq.heappush(minheap, end)

        return len(minheap)