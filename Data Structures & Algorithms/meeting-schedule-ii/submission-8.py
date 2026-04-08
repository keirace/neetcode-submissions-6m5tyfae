"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()

        # number of days can go up and down
        # keep track of the max number of days
        # intervals=[(1,5),(5,10),(10,15),(15,20)]

        s, e = 0, 0
        days = res = 0
        for _ in range(len(end)):
            # meeting
            if start[s] < end[e]:
                days += 1
                s += 1
            else:
                e += 1
                days -= 1
            res = max(days, res)
        return res
