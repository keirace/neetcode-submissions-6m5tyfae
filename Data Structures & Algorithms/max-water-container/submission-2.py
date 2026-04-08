class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxamount = 0
        l, r = 0, len(heights)-1
        while l < r:
            w = r-l
            if heights[l] > heights[r]:
                h = heights[r]
                r -= 1
            else:
                h = heights[l]
                l += 1
            area = w * h
            maxamount = max(maxamount, area)
        return maxamount