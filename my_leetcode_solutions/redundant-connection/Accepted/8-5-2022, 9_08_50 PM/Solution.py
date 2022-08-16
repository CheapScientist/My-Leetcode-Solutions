// https://leetcode.com/problems/redundant-connection

class Solution:
    
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.parent = [-1]*(n + 1)
        for u, v in edges:
            ans = self.union(self.parent, u, v)
            if ans:
                return ans
        return [-1, -1]
            
        
    def find(self, parent, u):
        children = [u]
        while parent[u] > 0:
            u = parent[u]
            children.append(u)
        return u, children
    
    def union(self, parent: List[int], u: int, v: int) -> List[int]:
        paru, childrenu = self.find(parent, u)
        parv, childrenv = self.find(parent, v)
        # case 1: if weight of paru is greater than that of parv 
        if paru == parv:
            return [u, v]
        if abs(paru) > abs(parv):
            parent[paru] -= len(childrenv)
            for child in childrenv:
                parent[child] = paru
        else:
            parent[parv] -= len(childrenu)
            for child in childrenu:
                parent[child] = parv
        return 