class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums) - 1
        nums.sort()

        for i in range(n-1):
            j, k = i + 1, n
            if nums[i] > 0: # it's sorted, won't find anything sum up to 0
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                currsum = nums[i] + nums[j] + nums[k]
                if currsum < 0:
                    j += 1
                elif currsum > 0:
                    k -= 1
                else: # currsum == 0
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return res