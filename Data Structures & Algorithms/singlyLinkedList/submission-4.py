class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        for _ in range(index):
            if not curr:
                return -1
            curr = curr.next
        return curr.val if curr else -1

    def insertHead(self, val: int) -> None:
        curr = self.head
        new_node = Node(val, curr.next)
        curr.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        prev, curr = self.head, self.head.next
        for _ in range(index):
            if not curr:
                return False
            prev = curr
            curr = curr.next

        if curr:
            prev.next = curr.next
            if not prev.next:
                self.tail = prev
            return True
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res