// https://leetcode.com/problems/min-cost-to-connect-all-points

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        adj = { i:[] for i in range(l) }
        for i in range(l):
            x1, y1 = points[i]
            for j in range(i + 1, l):
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([weight, j])
                adj[j].append([weight, i])

        res = 0
        minHeap = [[0, 0]]
        visit = set()
        while len(visit) < l:
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for neiCost, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        return res