class Solution:
    def countSubstrings(self, s: str) -> int:
        # two pointers even odd
        # Time O(n^2)
        count = [0]
        n = len(s)
        def span(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                count[0] += 1

        for i in range(n):
            # odd
            span(i, i)
            # even
            span(i, i+1)
        return count[0]