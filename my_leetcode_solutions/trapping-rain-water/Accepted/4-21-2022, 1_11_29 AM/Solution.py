// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        Lmax = []
        Rmax = []
        l = len(height)
        ans = 0
        
        for i in height:
            L = Lmax[-1] if Lmax else 0
            Lmax.append(max(L, i))
        for i in height[::-1]:
            R = Rmax[-1] if Rmax else 0
            Rmax.append(max(R, i))
        Rmax = Rmax[::-1]
        for i in range(l):
            vol = min(Rmax[i], Lmax[i]) - height[i]
            ans += max(vol, 0)
        return ans