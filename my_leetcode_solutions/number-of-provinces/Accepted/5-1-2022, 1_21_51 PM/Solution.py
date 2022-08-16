// https://leetcode.com/problems/number-of-provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [-1]*(len(isConnected))
        n = len(isConnected)
        visit = set()
        
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
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and (i, j) not in visit:
                    visit.add((i, j))
                    visit.add((j, i))
                    union(i, j)
        ans = 0
        for i in parent:
            if i < 0:
                ans += 1
        return ans
        