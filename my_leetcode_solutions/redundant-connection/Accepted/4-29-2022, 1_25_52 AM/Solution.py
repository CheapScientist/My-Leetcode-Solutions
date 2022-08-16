// https://leetcode.com/problems/redundant-connection

class Solution:
    def findRedundantConnection(self, edges):
        dsu = DSU(len(edges) + 1)
        for u, v in edges:
            if not dsu.union(u, v):
                return u, v


class DSU:
    def __init__(self, n):
        self.parent = [-1]*n

    def findUntil_parent(self, u: int):
        temp = []
        while self.parent[u] > 0:
            temp.append(u)
            u = self.parent[u]
        # we finally return the real parent u, all the childs we can find so far as [u, temp]
        return u, temp

    def union(self, u, v):
        pu, tempu = self.findUntil_parent(u)
        pv, tempv = self.findUntil_parent(v)
        if pu == pv:
            return False
        if abs(self.parent[pu]) > abs(self.parent[pv]):
            self.parent[pv] = pu
            for j in tempv:
                self.parent[j] = pu
            self.parent[pu] -= len(tempv)
        else:
            self.parent[pu] = pv
            for j in tempv:
                self.parent[j] = pv
            self.parent[pv] -= len(tempu)
        return True