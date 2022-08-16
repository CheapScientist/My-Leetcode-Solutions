// https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.path = []
        
        def dfs(i):
            if len(self.path) == k:
                self.ans.append(self.path[:])
                return
            for j in range(i, n + 1):
                self.path.append(j)
                dfs(j + 1)
                self.path.pop()
        dfs(1)
        return self.ans