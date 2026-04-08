class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # find a cycle
        visiting = set()
        # course to prereq
        premap = defaultdict(list)
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        def dfs(course):
            if course in visiting: # cycle
                return False
            
            visiting.add(course)
            for pre in premap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            premap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True