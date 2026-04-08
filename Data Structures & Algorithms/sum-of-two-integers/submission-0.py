class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            # start from the left
            bit1 = a & 1
            bit2 = b & 1
            curr = bit1 ^ bit2 ^ carry
            if curr:
                res |= 1 << i
            # carry = 1
            # 1. both bits are 1
            # 2. either bits + carry >= 2
            if bit1 & bit2 or ((bit1 or bit2) and carry):
                carry = 1
            else:
                carry = 0
            a >>= 1
            b >>= 1

        return res if res < 0x7FFFFFFF else ~(res ^ mask)