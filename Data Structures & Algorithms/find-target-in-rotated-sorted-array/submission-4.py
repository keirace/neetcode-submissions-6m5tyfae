class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while l <= h:
            m = l+(h-l) // 2
            if nums[m] == target:
                return m

            print(nums[l], nums[m] , nums[h])
            # nums l -> m is sorted
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]: # shift right
                    l = m + 1
                else: # shift left
                    h = m - 1

            else:
                if target > nums[h] or target < nums[m]:
                    h = m - 1 # shift left
                else:
                    l = m + 1 # shift right
            
        return -1