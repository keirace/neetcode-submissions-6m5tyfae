class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minnum = 1
        while True:
            flag = True
            for i in nums:
                if i == minnum: # found
                    flag = False
                    break
            if flag: # number not found
                return minnum
            minnum += 1 # if num is found, try num+1