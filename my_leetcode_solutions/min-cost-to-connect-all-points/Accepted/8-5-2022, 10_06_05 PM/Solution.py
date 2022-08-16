// https://leetcode.com/problems/min-cost-to-connect-all-points

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 1. first create a graph
        adj = {tuple(x): [] for x in points}
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                m_dist = abs(x1 - x2) + abs(y1 - y2)
                adj[(x1, y1)].append([m_dist, (x2, y2)])
                adj[(x2, y2)].append([m_dist, (x1, y1)])
        
        # 2. implement Prim's algo
        visit = set()
        cost = 0
        minHeap = [(0, tuple(points[0]))] # current cost, current node
        
        while len(visit) < n:
            curCost, curNode = heapq.heappop(minHeap)
            if curNode in visit:
                continue
            cost += curCost
            visit.add(curNode)
            for neighbor in adj[curNode]:
                neiCost, nei = neighbor
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        return cost
        