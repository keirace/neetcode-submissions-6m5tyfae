class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # at most 2 numbers
        cand1 = cand2 = cnt1 = cnt2 = 0
        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
            # pick a new candidate
            elif cnt1 == 0:
                cand1 = num
                cnt1 += 1
            elif cnt2 == 0:
                cand2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        # verify the counts
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
        
        res = []
        n = len(nums)
        # verify if each number appears more than n//3
        if cnt1 > n // 3:
            res.append(cand1)
        if cnt2 > n // 3:
            res.append(cand2)
        
        return res
            