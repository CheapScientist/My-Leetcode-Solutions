// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites:list[list[int]]):
        indegrees = [0 for _ in range(numCourses)]
        adj = { i: [] for i in range(numCourses)}

        for crs, prereq in prerequisites:
            adj[prereq].append(crs)
            indegrees[crs] += 1
        q = deque()
        for i, j in enumerate(indegrees):
            if j == 0:
                q.append(i)
        while q:
            cur = q.pop()
            numCourses -= 1
            for nextC in adj[cur]:
                indegrees[nextC] -= 1
                if indegrees[nextC] == 0:
                    q.append(nextC)


        return True if numCourses == 0 else False