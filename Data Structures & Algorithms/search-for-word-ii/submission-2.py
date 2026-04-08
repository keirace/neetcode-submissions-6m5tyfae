class Node():
    def __init__(self):
        self.children = {}
        self.end = False

    def addword(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        rows, cols = len(board), len(board[0])
        res = set()
        def backtrack(r, c, node, word):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] not in node.children:
                return

            temp = board[r][c]
            board[r][c] = '#' # mark visited
            word += temp
            node = node.children[temp]
            if node.end:
                res.add(word)

            backtrack(r+1, c, node, word)
            backtrack(r-1, c, node, word)
            backtrack(r, c+1, node, word)
            backtrack(r, c-1, node, word)
            board[r][c] = temp
        
        for word in words:
            root.addword(word)
            
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root, '')
        return list(res)
