class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        tcount = Counter(t)
        have, need = 0, len(tcount)
        window = defaultdict(int)
        minlen = math.inf
        res = [-1, -1]
        l = 0
        for r in range(len(s)): # run thru all s; as there might be better choice
            window[s[r]] += 1
            if s[r] in tcount and window[s[r]] == tcount[s[r]]:
                have += 1

            while have == need:
                currlen = r-l+1
                if currlen < minlen: # update minlen, res if new window is smaller
                    minlen = currlen
                    res = [l, r]
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                if s[l] in tcount and window[s[l]] < tcount[s[l]]: # decrement have if hashmap no longer satisfy the required number of ch
                    have -= 1
                l += 1
        
        return s[res[0]:res[1]+1] if minlen != math.inf else ""