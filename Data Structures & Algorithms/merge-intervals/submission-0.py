class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            res_start, res_end = res[-1]
            # overlapping: ends first
            if res_end >= curr_start:
                res[-1][1] = max(res_end, curr_end)
            else:
                res.append(intervals[i])

        return res