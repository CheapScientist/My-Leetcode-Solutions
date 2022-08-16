// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        self.par = [-1]*n
        
        def find(u):
            temp = [u]
            while self.par[u] >= 0:
                u = self.par[u]
                temp.append(u)
            return u, temp
        
        for u, v in edges: 
            paru, tempu = find(u)
            parv, tempv = find(v)
            if paru == parv:
                continue
            else: 
                if abs(self.par[paru]) > abs(self.par[parv]):
                    for i in tempv:
                        self.par[i] = paru
                    self.par[paru] -= (len(tempv))
                else:
                    for i in tempu:
                        self.par[i] = parv
                    self.par[parv] -= (len(tempu))
        mx = 0
        s = []

        for i in self.par: 
            if i < 0: 
                s.append(-i)
        sm = sum(s)
        ans = 0
        for i in s: 
            ans += i*(sm - i)
        return ans//2
                