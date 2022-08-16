// https://leetcode.com/problems/longest-cycle-in-a-graph

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # kosaraju's algo
        n = len(edges)
        f_graph, b_graph = {i: [] for i in range(n)}, {j: [] for j in range(n)}
        for u, v in enumerate(edges):
            if v == -1: continue
            f_graph[u].append(v)
            b_graph[v].append(u)
        stack = []
        visit = set()
        
        def dfs(node):
            if node in visit: 
                return 
            visit.add(node)
            for neighbor in f_graph[node]:
                dfs(neighbor)
            stack.append(node)
            return
        
        for i in range(n):
            if i not in visit: 
                dfs(i)
        ans = 0
        visit2 = set()
        
        def dfs2(node):
            if node in visit2:
                return
            visit2.add(node)
            for neighbor in b_graph[node]:
                dfs2(neighbor)
            stack2.append(node)
            return 
        
        while stack:
            cur = stack.pop()
            if cur in visit2: 
                continue
            stack2 = []
            dfs2(cur)
            ans = max(ans, len(stack2))
        return ans if ans > 1 else -1
            
            