class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        max_safe = 2**31-1
        x *= sign
        while x:
            res = (res*10 + x % 10)
            if res > max_safe:
                return 0
            x //= 10

        return res * sign