# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        total = 0
        while curr:
            total += 1
            curr = curr.next

        index = total-n
        prevnode = None
        node = head
        for i in range(index):
            prevnode = node
            node = node.next
        
        if prevnode:
            prevnode.next = node.next
        else:
            head = node.next

        return head