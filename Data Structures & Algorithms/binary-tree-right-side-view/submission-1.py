# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root, level):
            if not root:
                return
            # dont append again if already added for that level
            if len(res) < level:
                # check if right exists else append left
                res.append(root.val)
            if root.right:
                dfs(root.right, level+1)
            if root.left:
                dfs(root.left, level+1)
        dfs(root, 1)
        return res