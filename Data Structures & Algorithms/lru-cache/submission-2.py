class LinkedList:
    # use node bc we need to access and add to front/back in O(1)
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # {int:Node}
        self.head, self.tail = LinkedList(0,0), LinkedList(0,0)
        self.head.next, self.tail.prev = self.tail, self.head
        # newest at the tail

    def get(self, key: int) -> int:
        # check if key exists?
        # no -> return -1
        if key not in self.cache:
            return -1
        # yes -> if cache[key] not at the tail.prev -> move
        if self.tail.prev != self.cache[key]:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        # remove the key if exists
        if key in self.cache:
            self.remove(self.cache[key])
        # append new one to the tail
        self.cache[key] = LinkedList(key, value)
        self.insert(self.cache[key])
        # within capacity?
        # no: pop the head and update the head pointer
        if len(self.cache) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]

    def remove(self, node):
        prev, nex = node.prev, node.next
        prev.next = nex
        nex.prev = prev
    
    def insert(self, node):
        prev, nex = self.tail.prev, self.tail
        prev.next = nex.prev = node
        node.next = nex
        node.prev = prev

