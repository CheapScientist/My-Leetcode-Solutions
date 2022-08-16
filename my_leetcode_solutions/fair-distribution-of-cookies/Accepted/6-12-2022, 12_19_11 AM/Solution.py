// https://leetcode.com/problems/fair-distribution-of-cookies

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        kids = [0]*k
        if len(cookies) == k:
            return max(cookies)

        def dfs(i):
            if i == len(cookies): 
                return max(kids)
            temp = float('inf')
            for k in range(len(kids)):
                kids[k] += cookies[i]
                temp = min(temp, dfs(i + 1))
                kids[k] -= cookies[i]
            return temp
        
        return dfs(0)