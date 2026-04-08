class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while i >= 0:
            digits[i] += carry
            if digits[i] // 10:
                carry = digits[i] // 10
                digits[i] %= 10
            else:
                carry = 0
            i -= 1
        
        if carry:
            digits.insert(0, carry)
        return digits