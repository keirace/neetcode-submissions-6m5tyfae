class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        k = math.floor(n / 3)
        counter = Counter(nums)
        res = []
        for num, cnt in counter.items():
            if cnt > k:
                res.append(num)
        return res