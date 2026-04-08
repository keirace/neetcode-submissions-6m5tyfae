class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # as many substring as possible
        hmap = {} # {ch: last appearing index}
        for i in range(len(s)):
            hmap[s[i]] = i
        
        res = []
        length = 0
        lastind = 0
        for i in range(len(s)):
            lastind = max(lastind, hmap[s[i]])
            length += 1
            if lastind == i:
                res.append(length)
                length = 0

        return res
        

