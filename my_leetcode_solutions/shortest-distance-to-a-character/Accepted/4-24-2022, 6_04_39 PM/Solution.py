// https://leetcode.com/problems/shortest-distance-to-a-character

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ll, rr = [], []
        ans = []
        recentC = -1
        for i, j in enumerate(s):
            if j == c:
                recentC = i
            if recentC < 0: 
                ll.append(float(inf))
            else:
                ll.append(i - recentC)
        recentC = -1
        for i, j in enumerate(s[::-1]):
            if j == c:
                recentC = i
            if recentC < 0: 
                rr.append(float(inf))
            else:
                rr.append(i - recentC)
        
        for i, j in enumerate(s):
            if j == c:
                ans.append(0)
            else:
                ans.append(min(rr[len(s) - i - 1], ll[i]))
        return ans