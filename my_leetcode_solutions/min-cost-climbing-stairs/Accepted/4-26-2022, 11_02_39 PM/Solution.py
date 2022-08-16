// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        oneStep = cost[-1]
        twoStep = 0
        for i in range(len(cost) - 2, -1, -1):
            tmp = oneStep
            oneStep = min(cost[i] + oneStep, cost[i] + twoStep)
            twoStep = tmp
        return min(twoStep, oneStep)