# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        dia = {None: (0, 0)}
        while stack:
            node = stack[-1]
            if node.left and node.left not in dia:
                stack.append(node.left)
            elif node.right and node.right not in dia:
                stack.append(node.right)
            else: # V L R
                node = stack.pop()
                left, leftdia = dia[node.left]
                right, rightdia = dia[node.right]

                dia[node] = (max(left, right) + 1, max(left + right, leftdia, rightdia))

        return dia[root][1]