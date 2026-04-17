# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        currhead = head
        prevtail = dummy
        
        while currhead:
            currtail = currhead
            for _ in range(k-1):
                # early return if not enough nodes
                currhead = currhead.next
                if currhead == None:
                    prevtail.next = currtail
                    return dummy.next

            # relink
            prevtail.next = currhead
            prevtail = currtail

            # reverse a group of k nodes
            prev = None
            for _ in range(k):
                temp = currtail.next
                currtail.next = prev
                prev = currtail
                currtail = temp
            
            currhead = currtail
        
        return dummy.next