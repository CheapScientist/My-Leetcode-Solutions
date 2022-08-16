// https://leetcode.com/problems/successful-pairs-of-spells-and-potions

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()
        n = len(potions)
        for i in range(len(spells)):
            cur = spells[i]
            pos = bisect_left(potions, success/cur)
            ans.append(n - pos)
        return ans