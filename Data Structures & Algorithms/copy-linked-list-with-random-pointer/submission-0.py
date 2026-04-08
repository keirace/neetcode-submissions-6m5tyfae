"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        store = {None:None}
        # 1st pass: map og to copy
        while curr:
            node = Node(curr.val)
            store[curr] = node
            curr = curr.next

        # 2nd pass: copy
        curr = head
        while curr:
            node = store[curr]
            node.next = store[curr.next]
            node.random = store[curr.random]
            curr = curr.next
        return store[head]
            

