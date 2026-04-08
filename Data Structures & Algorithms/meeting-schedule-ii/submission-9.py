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
        intervals.sort(key=lambda i:i.start)

        # end times of meetings in progress
        rooms = [intervals[0].end]
        for i in intervals[1:]:
            # room with the earliest end time is free
            if i.start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i.end)

        return len(rooms)