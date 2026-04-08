class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, word_i):
            if word_i == len(word):
                return True
            
            if i < 0 or i >= self.width or j < 0 or j >= self.height or board[i][j] != word[word_i] or board[i][j]=='#':
                return False
            
            # if word[word_i] == board[i][j]:
            #     word_i += 1
            
            board[i][j] = '#'
            res = (
                dfs(i+1, j, word_i+1) or
                dfs(i-1, j, word_i+1) or
                dfs(i, j+1, word_i+1) or
                dfs(i, j-1, word_i+1)
            )
            board[i][j] = word[word_i]
            return res

        res = []
        self.width, self.height = len(board), len(board[0])
        for i in range(self.width):
            for j in range(self.height):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False