class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while l < h:
            m = l+(h-l) // 2
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m
        pivot = l # smallest number index
        l, h = 0, len(nums)-1
        if target >= nums[pivot] and target <= nums[h]:
            l = pivot
        else:
            h = pivot - 1
            
        while l <= h:
            m = l+(h-l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1
            
        return -1