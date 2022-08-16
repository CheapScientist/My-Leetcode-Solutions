// https://leetcode.com/problems/redundant-connection

class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        self.par = [-1]*(1 + n)
        
        def find(u):
            temp = []
            while self.par[u] > 0:
                temp.append(u)
                u = self.par[u]
            return u, temp
        
        for u, v in edges: 
            foundU, foundV = find(u), find(v)
            paru, parv = foundU[0], foundV[0]
            tempu, tempv = foundU[1], foundV[1]
            if paru == parv:
                return [u, v]
            else: 
                if abs(self.par[paru]) > abs(self.par[parv]):
                    self.par[parv] = paru
                    for i in tempv:
                        self.par[i] = paru
                    if tempv: 
                        self.par[paru] -= (len(tempv))
                    else:
                        self.par[paru] -= 1
                else:
                    self.par[paru] = parv
                    for i in tempu:
                        self.par[i] = parv
                    if tempu: 
                        self.par[parv] -= (len(tempu))
                    else:
                        self.par[parv] -= 1
    
        return
        