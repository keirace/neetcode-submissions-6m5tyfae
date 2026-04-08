class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix suffix
        n = len(height)
        if n == 0:
            return 0
        prefixsum = [height[0]]*n
        suffixsum = [height[n-1]]*n
        for i in range(1, n):
            prefixsum[i] = max(prefixsum[i-1], height[i])

        for i in range(n-2, -1, -1):
            suffixsum[i] = max(suffixsum[i+1], height[i])
        
        res = 0
        for i in range(n):
            cap = min(prefixsum[i], suffixsum[i])
            if cap > height[i]:
                res += cap - height[i]
        return res