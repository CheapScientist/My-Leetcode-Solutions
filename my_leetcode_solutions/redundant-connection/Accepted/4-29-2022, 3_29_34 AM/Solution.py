// https://leetcode.com/problems/redundant-connection

class Solution:
    def findRedundantConnection(self, edges):
        parent = [-1]*(len(edges) + 1)
        
        def union(u, v):
            pu, tempu = findUntil_parent(u)
            pv, tempv = findUntil_parent(v)
            if pu == pv:
                return False
            if abs(parent[pu]) > abs(parent[pv]):
                parent[pv] = pu
                for j in tempv:
                    parent[j] = pu
                parent[pu] -= (len(tempv) + 1)
            else:
                parent[pu] = pv
                for j in tempu:
                    parent[j] = pv
                parent[pv] -= (len(tempu) + 1)
            return True
        
        def findUntil_parent(u: int):
            temp = []
            while parent[u] > 0:
                temp.append(u)
                u = parent[u]
            # we finally return the real parent u, all the childs we can find so far as [u, temp]
            return u, temp
        
        
        for u, v in edges:
            if not union(u, v):
                return u, v



