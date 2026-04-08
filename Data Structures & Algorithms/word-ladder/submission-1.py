class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        adjList = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:] # wild card at index j
                adjList[pattern].append(word)

        visited = set([beginWord])
        que = deque([(beginWord)])
        res = 0
        while que:
            res += 1
            for _ in range(len(que)): # by layer
                node = que.popleft()
                if node == endWord:
                    return res
                for j in range(len(word)):
                    pattern = node[:j] + '*' + node[j+1:]
                    for neighbor in adjList[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            que.append(neighbor)
                            print(que)
        return 0