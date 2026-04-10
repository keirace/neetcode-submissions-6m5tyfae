class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n == 0: return 0

        # initialize LPS array: prefix suffix
        # tells how many chars we can skip
        lps = [0] * n
        i = 1
        prevLPS = 0

        while i < n:
            # match; increment
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            # mismatch
            elif prevLPS == 0:
                # lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS-1]

        i = 0 # ptr for haystack
        j = 0 # ptr for pattern
        # inc i, j if match
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            elif j == 0:
                i += 1
            else:
                j = lps[j-1]
            
            if j == n:
                return i-n
        
        return -1