class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            res = 0
            while n:
                res += (n%10) ** 2
                n //= 10
            if res == 1:
                return True
            n = res
        return False
