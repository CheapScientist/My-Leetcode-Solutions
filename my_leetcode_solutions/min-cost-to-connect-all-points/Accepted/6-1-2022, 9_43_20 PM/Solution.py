// https://leetcode.com/problems/min-cost-to-connect-all-points

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # first create a graph, will be a hash map with neighbors like [weight, i]
        n = len(points)
        adj = {i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([weight, j])
                adj[j].append([weight, i])
        
        # now apply prim's algorithm
        visit = set()
        cost = 0
        minH = [(0, 0)] # current cost, current node
        
        while len(visit) < n:
            curCost, curNode = heappop(minH)
            if curNode in visit:
                continue
            cost += curCost
            visit.add(curNode)
            for neighbor in adj[curNode]:
                neiCost, nei = neighbor
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return cost
        