// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        if len(A) < 3: return []
        A.sort()
        n = len(A)
        ans = []
        used = set()
                
        def two_sum(l, r, target):
            res = []
            while l < r:
                a, b = A[l], A[r]
                if a + b == target:
                    res.append([a, b])
                    while r - 1 and A[r] == A[r - 1]:
                        r -= 1
                        
                    while l + 1 < n and A[l] == A[l + 1]:
                        l += 1
                        
                if a + b > target:
                    r -= 1
                else:
                    l += 1
            return res
        
        for i in range(n - 2):
            l, r = i + 1, n - 1
            if i and A[i] == A[i - 1]:
                continue
            res = two_sum(l, r, -A[i])
            if not res: 
                continue
            for j in res: 
                ans.append([A[i]] + j)
        return ans
        
