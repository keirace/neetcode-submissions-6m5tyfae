class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        longest = 0
        for i in nums:
            if i-1 in nums: # not the start of a sequence
                continue
            length = 0
            while i + length in nums:
                length += 1
            if length > longest:
                longest = length

        return longest