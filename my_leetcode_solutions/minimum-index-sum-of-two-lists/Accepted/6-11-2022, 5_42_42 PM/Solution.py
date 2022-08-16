// https://leetcode.com/problems/minimum-index-sum-of-two-lists

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        memo1, memo2 = {}, {}
        for i, j in enumerate(list1):
            memo1[j] = i
        for i, j in enumerate(list2):
            memo2[j] = i
        ans = {}
        for keys in memo1: 
            if keys in memo2: 
                ans[memo1[keys] + memo2[keys]] = ans.get(memo1[keys] + memo2[keys], []) + [keys]
        res = min(ans.keys())
        return ans[res]