# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, prevmax):
            if not root:
                return None
            if root.val >= prevmax:
                res.append(root.val)
                prevmax = root.val
            dfs(root.left, prevmax)
            dfs(root.right, prevmax)

        res = []
        dfs(root, float('-inf'))
        return len(res)