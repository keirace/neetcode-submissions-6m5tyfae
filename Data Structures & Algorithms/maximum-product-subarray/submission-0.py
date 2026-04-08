class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            temp = curMin
            curMin = min(curMax*n, n*curMin, n)
            curMax = max(curMax*n, n*temp, n)

            res = max(res, curMax)
        return res