class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # as many substring as possible
        count = Counter(s)
        res = []
        length = 0
        working = set()

        for ch in s:
            working.add(ch)
            count[ch] -= 1
            length += 1
            # all ch count[ch] == 0: split substring
            # else get another ch
            if all(not count[i] for i in working):
                res.append(length)
                length = 0
                working = set()

        return res