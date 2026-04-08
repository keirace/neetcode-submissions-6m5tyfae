# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            if not root:
                res.append('N')
                return
            res.append(str(root.val))
            dfs(root.left), dfs(root.right)
        res = []
        dfs(root)
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def dfs():
            nonlocal i
            if data[i] == 'N':
                i += 1
                return
            root = TreeNode(int(data[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root

        data = data.split(',')
        i = 0
        return dfs()