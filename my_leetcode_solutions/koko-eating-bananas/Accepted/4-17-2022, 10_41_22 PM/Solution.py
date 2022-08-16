// https://leetcode.com/problems/koko-eating-bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles): return max(piles)
        l ,r  = 1, max(piles)
        res = r
        while l <= r: 
            numHours = 0
            mi = (l + r)//2
            for i in piles:
                if i % mi == 0:
                    numHours += i//mi
                else:
                    numHours += i//mi + 1
            if numHours <= h:
                res = min(res, mi)
                r = mi - 1
            else:
                l = mi + 1
        return res