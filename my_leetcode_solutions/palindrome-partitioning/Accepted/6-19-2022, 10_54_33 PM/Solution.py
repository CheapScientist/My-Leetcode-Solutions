// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        build = []
        n = len(s)
        
        def helper(i, j): # inclusive, inclusive
            if j == i: return True

            l, r = i, j
            while l <= r: 
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True
        

        
        def dfs(i):
            if i == n: 
                ans.append(build[:])
                return 
            for j in range(i, n): 
                if helper(i, j): 
                    build.append(s[i:j+1])
                    dfs(j + 1)
                    build.pop()
            return 
        
        dfs(0)
        return ans