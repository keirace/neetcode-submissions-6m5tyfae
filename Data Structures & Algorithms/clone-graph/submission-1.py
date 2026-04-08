"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        clone = {}
        # clone[node] = Node(node.val)
        def dfs(node):
            if node in clone:
                return clone[node]
            
            clone[node] = Node(node.val)
            for n in node.neighbors:
                neighbor_node = dfs(n)
                clone[node].neighbors.append(neighbor_node)
            return clone[node]
        return dfs(node)