// https://leetcode.com/problems/sum-of-numbers-with-units-digit-k

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num < 0: return -1
        if not num: return 0
        if not k: 
            return 1 if not num%10 else -1
        @cache
        def dfs(num, k):
            if num < 0: return float('inf')
            if not num: return 0
            if num < 10: 
                return num//k if not num%k else float('inf')
            m = num//10
            ans = float('inf')
            for i in range(m, -1, -1): 
                ans = min(ans, 1 + dfs(num-(10*i+k), k))
            return ans
        ans = dfs(num, k)
        return ans if ans != float('inf') else -1
            
            