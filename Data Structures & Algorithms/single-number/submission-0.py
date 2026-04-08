class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR - a pair of numbers will clear each other out
        res = 0
        for num in nums:
            res = num ^ res # true when diff
        return res