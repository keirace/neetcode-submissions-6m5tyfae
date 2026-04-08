class Node():
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.endofword = True

    def search(self, word: str) -> bool:
        # wihout dfs it would return False if the testing child does not match
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                if word[i] == '.':
                    for val in curr.children.values():
                        if dfs(i+1, val):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.endofword
        return dfs(0, self.root)