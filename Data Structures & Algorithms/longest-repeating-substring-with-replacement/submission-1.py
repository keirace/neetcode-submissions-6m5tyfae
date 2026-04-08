class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        longest, maxf = 0, 0
        counter = {}
        for j in range(len(s)):
            counter[s[j]] = 1 + counter.get(s[j], 0)
            maxf = max(maxf, counter[s[j]])
            while (j-i+1) - maxf > k: # number of ch to replace
                counter[s[i]] -= 1
                i += 1 # shrink the window
            longest = max(j-i+1, longest)

        return longest