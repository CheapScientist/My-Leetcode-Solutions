// https://leetcode.com/problems/permutations-ii

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()      
        
        def dfs(path, remain):
            if not remain: 
                res.append(path[:])
                return 
            for i in range(len(remain)): 
                if i > 0 and remain[i - 1] == remain[i]:
                    continue
                dfs(path + [remain[i]], remain[:i] + remain[i + 1:])
            return 
        
        dfs([], nums)
        return res