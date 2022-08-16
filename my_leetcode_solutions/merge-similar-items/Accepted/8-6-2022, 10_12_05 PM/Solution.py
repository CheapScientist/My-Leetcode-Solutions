// https://leetcode.com/problems/merge-similar-items

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ans = {}
        for i, j in items1:
            ans[i] = ans.get(i, 0) + j
        for i, j in items2:
            ans[i] = ans.get(i, 0) + j
        res = [[key, ans[key]] for key in ans]
        res.sort()
        return res