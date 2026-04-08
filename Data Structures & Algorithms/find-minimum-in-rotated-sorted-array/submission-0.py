class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find now many times the array has been rotated
        l, h = 0, len(nums) - 1
        while l < h:
            m = l+(h-l) // 2
            if nums[m] < nums[h]:
                h = m
            else:
                l = m + 1
        return nums[l]


