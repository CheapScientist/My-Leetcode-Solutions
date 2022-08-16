// https://leetcode.com/problems/jump-game-iii

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visit = set()
        @cache
        def dfs(i):
            if not (len(arr) > i >= 0) or i in visit:
                return False
            visit.add(i)
            if arr[i] == 0:
                return True
            return dfs(i - arr[i]) or dfs(i + arr[i])
        return dfs(start)
        