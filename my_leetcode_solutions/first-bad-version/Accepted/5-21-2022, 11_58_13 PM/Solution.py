// https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        
        while l <= r:
            mi = (l + r)//2
            if not isBadVersion(mi):
                l = mi + 1
            else:
                r = mi - 1
        return l