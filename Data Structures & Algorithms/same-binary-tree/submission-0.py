# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True
            if p and q:
                left, right = dfs(p.left, q.left), dfs(p.right, q.right)
                if left and right and p.val == q.val:
                    return True
            return False

        return dfs(p, q)