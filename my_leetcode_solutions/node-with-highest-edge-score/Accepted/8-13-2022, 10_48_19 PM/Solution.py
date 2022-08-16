// https://leetcode.com/problems/node-with-highest-edge-score

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        ans = [0]*n
        for idx, edge in enumerate(edges):
            ans[edge] += idx
        mx = 0
        res = 0
        for i, j in enumerate(ans):
            if j > mx:
                res = i
                mx = j
        return res