// https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        
        def dfs(i, curTotal):
            if curTotal > target:
                return
            if curTotal == target:
                res.append(subset[:])
                return
            if i == len(candidates):
                return
            subset.append(candidates[i])
            dfs(i + 1, curTotal + candidates[i])
            subset.pop()
            while (i + 1 in range(len(candidates)) and 
                   candidates[i] == candidates[i + 1]):
                i += 1
            dfs(i + 1, curTotal)
            
        dfs(0, 0)
        return res