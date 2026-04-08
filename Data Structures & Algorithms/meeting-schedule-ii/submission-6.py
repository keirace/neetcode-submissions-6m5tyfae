"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        use min heap to keep track of the earliest end and the number of meetings
        if earliest <= start; no conflicts
            pop old end -> number of meetings - 1
        push in new end -> number of meetings + 1
        count elements in the heap at the end
        '''
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        minheap = []

        for i in intervals:
            if minheap and minheap[0] <= i.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, i.end)

        return len(minheap)