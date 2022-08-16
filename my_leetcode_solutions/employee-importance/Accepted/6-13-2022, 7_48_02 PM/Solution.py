// https://leetcode.com/problems/employee-importance

class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        adj = {}
        memo = {}
        for employee in employees:
            memo[employee.id] = employee
            adj[employee] = employee.subordinates
        visit = set()

        def dfs(node: Employee):
            if node not in adj or node in visit:
                return 0
            visit.add(node)
            ans = node.importance
            for nei in adj[node]:
                ans += dfs(memo[nei])
            return ans

        return dfs(memo[id])