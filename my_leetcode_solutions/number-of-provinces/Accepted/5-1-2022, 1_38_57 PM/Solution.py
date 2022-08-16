// https://leetcode.com/problems/number-of-provinces

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]):
        n = len(isConnected)
        graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i > j:
                    graph[i].append(j)
                    graph[j].append(i)
        visit = set()

        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for nei in graph[i]:
                dfs(nei)

        ans = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                ans += 1
        return ans