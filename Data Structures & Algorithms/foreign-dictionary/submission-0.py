class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # dfs sol
        adjlist = {ch:set() for w in words for ch in w}
        for i in range(len(words)-1):
            # grab a pair of words then check for the first diff pair of chars
            w1, w2 = words[i], words[i+1]
            length = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:length] == w2[:length]:
                return ""  # invalid ordering
            for j in range(length):
                if w1[j] != w2[j]:
                    adjlist[w1[j]].add(w2[j])
                    break
        
        state = {} # 0:unvisited 1: visiting 2: visited
        ordering = []
        def dfs(v):
            if state.get(v) == 1: # cycle
                return False
            if state.get(v) == 2: # already processed
                return True
            state[v] = 1
            for neighbor in adjlist[v]:
                if not dfs(neighbor):
                    return False
            state[v] = 2
            ordering.append(v)
            return True
        
        for j in adjlist:
            if state.get(j, 0) == 0: # unvisited
                if not dfs(j):
                    return ""

        ordering.reverse()
        return "".join(ordering)


                
