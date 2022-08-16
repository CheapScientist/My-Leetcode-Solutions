// https://leetcode.com/problems/top-k-frequent-words

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        memo = {}
        for i in words: 
            memo[i] = memo.get(i, 0) + 1
        ans = []
        for key in memo: 
            ans.append([memo[key], key])
        ans.sort(key = lambda x: (-x[0], x[1]))
        res = []
        for i in range(k): 
            res.append(ans[i][1])
        return res