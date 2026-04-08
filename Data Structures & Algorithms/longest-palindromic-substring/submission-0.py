class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        maxlen = 0
        n = len(s)
        for i in range(n):
            # odd palindrome
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > maxlen:
                    maxlen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
            
            # even
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > maxlen:
                    maxlen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
        return res