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
                return True
            if crs in visited:
                return False
            visited.add(crs)
            visiting.add(crs)
            for pre in preMap[crs]:
                if dfs(pre): return True
            visiting.remove(crs)
            
            return False
        
        for c in range(numCourses):
            if dfs(c): return False
        return True