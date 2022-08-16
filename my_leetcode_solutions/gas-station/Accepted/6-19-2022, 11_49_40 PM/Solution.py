// https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        localMin = float('inf')
        n = len(gas)

        for idx, g in enumerate(gas):
            c = cost[idx]
            total += g - c
            if total < localMin:
                localMin = total
                if idx == n - 1:
                    ans = 0
                else:
                    ans = idx + 1

        return ans if total >= 0 else -1