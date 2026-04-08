# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        res = head
        carry = 0

        while l1 and l2:
            val = l1.val + l2.val + carry
            res.next = ListNode(val % 10)
            if val >= 10:
                carry = 1
            else:
                carry = 0
            res = res.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + carry
            res.next = ListNode(val % 10)
            carry = 1 if val >= 10 else 0
            l1 = l1.next
            res = res.next

        while l2:
            val = l2.val + carry
            res.next = ListNode(val % 10)
            carry = 1 if val >= 10 else 0
            l2 = l2.next
            res = res.next

        if 1 == carry:
            res.next = ListNode(carry)

        return head.next