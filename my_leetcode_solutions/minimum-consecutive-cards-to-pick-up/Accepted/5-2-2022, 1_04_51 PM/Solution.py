// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        memo = {}
        ans = []
        for i, j in enumerate(cards):
            if j in memo:
                ans.append(i - memo[j] + 1)
                memo[j] = i
            else:
                memo[j] = i
        return min(ans) if ans else -1