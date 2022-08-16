// https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i:[] for i in range(numCourses)} 
        
        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        self.res = []
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
            self.res.append(crs)
            return False
        
        for c in range(numCourses):
            if dfs(c): return []
        return self.res