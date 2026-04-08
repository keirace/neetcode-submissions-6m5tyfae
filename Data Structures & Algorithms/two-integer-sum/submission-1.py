class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {} # {num:index}
        for i, n in enumerate(nums):
            if target - n in hmap:
                return [hmap[target - n], i]
            hmap[n] = i