// https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for _ in range(numCourses)]
        adj = { i: [] for i in range(numCourses)}
        ans = []
        
        for crs, prereq in prerequisites:
            adj[prereq].append(crs)
            indegrees[crs] += 1
        q = deque()
        for i, j in enumerate(indegrees):
            if j == 0:
                q.append(i)
        while q:
            cur = q.pop()
            ans.append(cur)
            numCourses -= 1
            for nextC in adj[cur]:
                indegrees[nextC] -= 1
                if indegrees[nextC] == 0:
                    q.append(nextC)


        return ans if numCourses == 0 else []