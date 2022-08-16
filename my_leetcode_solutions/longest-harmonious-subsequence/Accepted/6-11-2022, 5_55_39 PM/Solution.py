// https://leetcode.com/problems/longest-harmonious-subsequence

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums: return 0
        memo = {}
        for i in nums: 
            memo[i] = memo.get(i, 0) + 1
        res = 0
        for i in nums: 
            temp = memo[i]
            if i + 1 in memo: 
                temp += memo[i + 1]
                res = max(res, temp)
            temp = memo[i]
            if i - 1 in memo: 
                temp += memo[i - 1]
                res = max(res, temp)
            if i + 1 not in memo and i - 1 not in memo:
                continue

        return res