// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = { i:[] for i in range(numCourses)} 
        
        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()
        visited = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            visited.add(crs)
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visiting.remove(crs)
            
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        return True