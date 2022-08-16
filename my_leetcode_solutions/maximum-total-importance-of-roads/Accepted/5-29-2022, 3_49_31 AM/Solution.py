// https://leetcode.com/problems/maximum-total-importance-of-roads

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        adj = {i:[[]] for i in range(n)}
        w = []
        for i in range(n):
            w.append([i, 0]) # idx, weight
        weightLeft = n
        for u, v in roads:
            adj[u][0].append(v)
            w[u][1] += 1
            w[v][1] += 1
            adj[v][0].append(u)
        w.sort(key = lambda x: x[1], reverse = True)
        for i in w:
            idx, _ = i
            adj[idx].append(weightLeft)
            weightLeft -= 1
        ans = 0
        visit = set()
        
        def dfs(i):
            if i in visit:
                return 0
            visit.add(i)
            neighbors, weight = adj[i]
            temp = 0
            for nei in neighbors:
                temp += weight + dfs(nei)
            return temp
        
        for i in range(n):
            if i not in visit:
                ans += dfs(i)
        return ans

        