// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        
        dp = [0]*(n + 1) 
        for i in range(1, n + 1):
            dp[i] = ord(s1[i - 1]) + dp[i - 1]
        # for j in range(1, m + 1):
        #     dp[j][0] = ord(s2[j - 1]) + dp[j - 1][0]
        for r in range(1, m + 1): 
            temp = []
            temp.append(ord(s2[r - 1]) + dp[0])
            for c in range(1, n + 1): 
                if s1[c - 1] == s2[r - 1]:
                    temp.append(dp[c - 1])
                else:
                    ans = min(ord(s2[r - 1]) + dp[c], ord(s1[c - 1]) + temp[-1])
                    temp.append(ans)
            dp = temp[:]
        # print(dp)
        return dp[-1]
        
