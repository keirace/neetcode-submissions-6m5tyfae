class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = [[] for i in range(numCourses)]
        # indegree
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            indegree[crs]+=1
            adjlist[pre].append(crs)

        # append nodes with 0 incoming degree
        que = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)
        
        order = []
        finish = 0
        # loop que and decrease indegree, append if no neigbor left
        while que:
            node = que.popleft()
            order.append(node)
            finish += 1
            for neighbor in adjlist[node]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    que.append(neighbor)
        
        return order if finish == numCourses else []