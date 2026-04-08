class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # dependency resolution problem
        adj = {ch: set() for w in words for ch in w}
        in_degree = {ch: 0 for w in words for ch in w}

        # build a graph
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            minlen = min(len(word1), len(word2))
            # edge case: can't sort if longer word with the same prefix comes first
            # ex. apple and app
            if len(word1) > len(word2) and word1[:minlen] == word2[:minlen]:
                return ''
            
            for i in range(minlen):
                if word1[i] != word2[i]:
                    # found the first diff word1[i]->word2[i]
                    if word2[i] not in adj[word1[i]]:
                        adj[word1[i]].add(word2[i])
                        in_degree[word2[i]] += 1
                    break # stop comparing the pair after the first diff

        # kahn's algorithm
        que = deque([ch for ch in in_degree if in_degree[ch] == 0])
        res = ''

        while que:
            ch = que.popleft()
            res += ch
            for nei in adj[ch]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    que.append(nei)
        
        # cycle check
        if len(res) != len(in_degree):
            return ''
        
        return res
