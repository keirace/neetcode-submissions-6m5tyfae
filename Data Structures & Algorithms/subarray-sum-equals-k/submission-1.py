class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # can be solved with recursion or prefix sum
        pathsum = {0:1} # sum : number of ways
        currsum = 0
        res = 0

        for n in nums:
            currsum += n
            res += pathsum.get(currsum - k, 0)
            pathsum[currsum] = pathsum.get(currsum, 0) + 1

        return res