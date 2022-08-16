// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        fab = []
        fab.append(1)
        fab.append(1)
        for i in range(2, n + 1):
            fab.append( fab[i - 1] + fab[i - 2])
        return fab[n]