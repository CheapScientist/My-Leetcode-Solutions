// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res = 0
        new = []
        for cap, rock in zip(capacity, rocks):
            if cap > rock:
                new.append(cap - rock)
            elif cap == rock:
                res += 1
            else:
                continue
        n = len(new)
        @cache
        def dfs(i, curVal):
            if i == n or curVal == 0:
                return 0
            if curVal - new[i] >= 0:
                a1 = 1 + dfs(i + 1, curVal - new[i])
            else:
                a1 = float('-inf')
            a2 = dfs(i + 1, curVal)
            return max(a1, a2)
        return res + dfs(0, additionalRocks)
            
        
        