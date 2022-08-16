// https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits: return 0
        ans, l = 0, 0
        n = len(fruits)
        seen = {}
        for r in range(n):
            seen[fruits[r]] = seen.get(fruits[r], 0) + 1
            while len(seen) > 2:
                seen[fruits[l]] -= 1
                if not seen[fruits[l]]:
                    del seen[fruits[l]]
                l += 1
            
            ans = max(ans, r - l + 1)
        return ans