class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0 # window

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1): # level
                farthest = max(nums[i]+i, farthest)
            l = r+1
            r = farthest
            res += 1 # similar to level
        return res