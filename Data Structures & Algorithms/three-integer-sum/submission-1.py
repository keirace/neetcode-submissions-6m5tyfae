class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums) - 1
        nums.sort()

        for i in range(n-1):
            j, k = i + 1, n
            if nums[i] > 0: # it's sorted, won't find anything sum up to 0
                break
            while j < k:
                currsum = nums[i] + nums[j] + nums[k]
                if currsum < 0:
                    j += 1
                elif currsum > 0:
                    k -= 1
                else: # currsum == 0
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

        return res