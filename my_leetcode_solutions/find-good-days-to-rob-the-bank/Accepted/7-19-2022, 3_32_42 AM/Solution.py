// https://leetcode.com/problems/find-good-days-to-rob-the-bank

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        ans = []
        left_days, right_days = [0]*n, [0]*n
        
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left_days[i] = 1 + left_days[i - 1]
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right_days[i] = 1 + right_days[i + 1]
        for i in range(n):
            if i < time or (n - i - 1) < time:
                continue
            if left_days[i] >= time and right_days[i] >= time:
                ans.append(i)

        return ans