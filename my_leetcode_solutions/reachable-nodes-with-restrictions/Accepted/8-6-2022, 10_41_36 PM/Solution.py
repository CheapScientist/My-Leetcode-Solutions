// https://leetcode.com/problems/reachable-nodes-with-restrictions

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], A: List[int]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        rs = set(A)
        ans = 0
        visit = set([0])
        
        q = deque([0])
        while q: 
            cur = q.pop()
            ans += 1
            for child in adj[cur]:
                if child not in visit and child not in rs:
                    visit.add(child)
                    q.append(child)
        return ans

#         def dfs(node):
#             if node not in adj or node in A:
#                 return 

#             self.ans += 1
#             if node in adj: 
#                 for child in adj[node]:
#                     if child not in visit:
#                         visit.add(child)
#                         dfs(child)
#         dfs(0)
#         return self.ans