"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # heap
        if not intervals:
            return 0
        
        intervals.sort(key=lambda i:i.start)
        ends = []

        for i in intervals:
            # if meeting starts after earliest end
            if ends and i.start >= ends[0]:
                heapq.heappop(ends) # reuse the room
            heapq.heappush(ends, i.end)

        return len(ends)
                