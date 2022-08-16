// https://leetcode.com/problems/path-with-maximum-probability

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = {i:[] for i in range(n)}
        m = len(edges)
        for i in range(m):
            u, v = edges[i]
            prob = succProb[i]
            adj[u].append([prob, v]) # push in like [prob, vert]
            adj[v].append([prob, u])
        maxHeap = [[-1, start]]
        ans = 0.0
        visit = {start: 1}

        while maxHeap:

            curProb, curNode = heapq.heappop(maxHeap)
            curProb *= -1
            if curNode == end:
                return curProb
            for child in adj[curNode]:
                childProb, childNode = child
                if childNode not in visit or visit[childNode] < childProb * curProb:
                    visit[childNode] = childProb * curProb
                    heapq.heappush(maxHeap, [-childProb * curProb, childNode])
            
        return ans
        