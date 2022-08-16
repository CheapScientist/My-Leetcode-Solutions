// https://leetcode.com/problems/ugly-number-iii

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        dp = [1]*(n+1)
        xa, xb, xc = 1, 1, 1
        for i in range(1, n+1):
            print(xa, xb, xc)
            aa, bb, cc = a*xa, b*xb, c*xc
            dp[i] = min(aa, bb, cc)
            if dp[i] == aa: xa += 1
            if dp[i] == bb: xb += 1
            if dp[i] == cc: xc += 1
        print(dp)
        return dp[-1]
            
        