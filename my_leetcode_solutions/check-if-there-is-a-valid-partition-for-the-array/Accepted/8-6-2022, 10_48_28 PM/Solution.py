// https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array

class Solution:
    def validPartition(self, A: List[int]) -> bool:
        n = len(A)
        
        @cache
        def dfs(i):
            if i == n:
                return True
            if i > n:
                return False
            ans = False
            if i + 1 < n and i + 2 < n and (A[i + 1] == A[i + 2] == A[i] or (A[i + 1] - A[i] == 1 and A[i + 2] - A[i + 1] == 1)):
                ans = ans or dfs(i + 3)
                if ans: 
                    return ans
            if i + 1 < n and A[i + 1] == A[i]:
                ans = ans or dfs(i + 2)
                if ans:
                    return ans
            return False
        
        return dfs(0)
