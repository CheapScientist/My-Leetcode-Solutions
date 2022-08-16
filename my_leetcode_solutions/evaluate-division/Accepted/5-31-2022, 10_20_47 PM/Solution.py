// https://leetcode.com/problems/evaluate-division

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]):
        # get an adj
        adj = defaultdict(dict)
        for i in range(len(values)):
            u, v = equations[i]
            val = values[i]
            adj[u][v] = val
            adj[v][u] = 1/val
        # dfs 
        ans = []
        def dfs(cur, target, visit):
            if cur not in adj or target not in adj:
                return -1.0
            if cur == target:
                return 1.0
            if cur in visit:
                return -1.0
            visit.add(cur)
            for i in adj[cur]:
                temp = dfs(i, target, visit)
                if temp < 0: 
                    continue
                else:   
                    return temp*adj[cur][i]
            return -1.0
        
        for u, v in queries:
            ans.append(dfs(u, v, set()))
        return ans