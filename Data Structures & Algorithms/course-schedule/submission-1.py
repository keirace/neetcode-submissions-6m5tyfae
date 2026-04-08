class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kanhn's algorithm
        indegree = [0]*numCourses
        # Adjacency lists cause this is not node
        adj = [[] for _ in range(numCourses)]

        # 1. initialize an incoming degree array
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        # 2. append any course with indegree = 0
        que = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                que.append(n)
        
        # 3. loop over que and decrease neighbor's indegree
        # until reaching 0, then append to the que
        # also keep track of finish
        finish = 0
        while que:
            course = que.popleft()
            finish += 1
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    que.append(neighbor)
        return finish == numCourses

        