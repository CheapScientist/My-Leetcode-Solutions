// https://leetcode.com/problems/redundant-connection

class Solution:
    def findRedundantConnection(self, edges):
        self.par = [-1]*(1 + len(edges))
        
        def find(u):
            temp = [u]
            while self.par[u] > 0:
                u = self.par[u]
                temp.append(u)
            return u, temp
        
        for u, v in edges: 
            paru, tempu = find(u)
            parv, tempv = find(v)
            if paru == parv:
                return [u, v]
            else: 
                if abs(self.par[paru]) > abs(self.par[parv]):
                    for i in tempv:
                        self.par[i] = paru
                    self.par[paru] -= (len(tempv))
                else:
                    for i in tempu:
                        self.par[i] = parv
                    self.par[parv] -= (len(tempu))