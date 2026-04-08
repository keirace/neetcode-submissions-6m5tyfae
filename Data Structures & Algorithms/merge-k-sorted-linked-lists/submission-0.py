# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for ls in lists:
            while ls:
                res.append(ls.val)
                ls = ls.next
        res.sort()

        root = curr = ListNode()
        for i in res:
            curr.next = ListNode(i)
            curr = curr.next
        return root.next