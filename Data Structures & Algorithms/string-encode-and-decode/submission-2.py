class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        enc = ''
        for s in strs:
            enc += str(len(s))
            enc += '#' # indicate the start in case len(s) > 10
            enc += s
        return enc


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            # string
            i = j + 1
            j = size+i
            res.append(s[i:j])
            i = j
        return res
