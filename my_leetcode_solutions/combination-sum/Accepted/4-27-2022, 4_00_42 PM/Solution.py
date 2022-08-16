// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
            dfs(i, curTotal + candidates[i])
            subset.pop()
            dfs(i + 1, curTotal)
            
        dfs(0, 0)
        return res