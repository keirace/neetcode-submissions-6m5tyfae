"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts, ends = [], []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        res = count = 0
        s, e = 0, 0
        print(starts, ends)

        while s < len(intervals):
            if starts[s] < ends[e]: # add a meeting
                s+=1
                count+=1
            else: # meeting ended
                e+=1
                count-=1
            res = max(count, res)

        return res