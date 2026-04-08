class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        hmap = {'{':'}', '(':')', '[':']'}
        for i in s:
            if i in hmap.keys():
                stack.append(i)
            elif i in hmap.values():
                if stack:
                    openbracket = stack.pop()
                    if i != hmap[openbracket]:
                        return False
                else:
                    return False
        return True if not stack else False