class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ''
        self.maxlen = 0
        n = len(s)

        def check(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > self.maxlen:
                    self.maxlen = r-l+1
                    self.res = palindrome = s[l:r+1]
                l-=1
                r+=1

        for i in range(n):
            # odd palindrome
            check(i, i)

            # even palindrome
            check(i, i+1)
        return self.res