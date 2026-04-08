# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        que = deque([root])
        while que:
            right = None
            for _ in range(len(que)):
                root = que.popleft() # FIFO
                right = root
                if root.left: que.append(root.left)
                if root.right: que.append(root.right) # last one to pop
            if right:
                res.append(right.val)
        return res