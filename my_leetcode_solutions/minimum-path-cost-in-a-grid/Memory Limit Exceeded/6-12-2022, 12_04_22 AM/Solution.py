// https://leetcode.com/problems/minimum-path-cost-in-a-grid

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        start, dest = set(grid[0]), set(grid[-1])
        m, n = len(grid), len(grid[0])
        adj = {i:[] for i in range(m*n)}
        for i in range(len(grid) - 1): 
            u = grid[i]
            v = grid[i + 1]
            for j in range(n): 
                for k in range(n):
                    adj[v[k]].append([moveCost[u[j]][k] + u[j], u[j]])
        minH = [] #cost, node
        for i in dest: 
            minH.append((i, i))
        while minH: 
            curCost, curNode = heapq.heappop(minH)
            if curNode in start: 
                return curCost
            neighbors = adj[curNode]
            for neiCost, nei in neighbors: 
                heapq.heappush(minH, (curCost + neiCost, nei))
        return -1