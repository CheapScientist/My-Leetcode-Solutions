// https://leetcode.com/problems/best-poker-hand

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        a1, a2, a3 = False, False, False
        if len(set(suits)) == 1:
            a1 = True
        B = Counter(ranks)
        if any(B[key] >= 3 for key in B):
            a2 = True
        if any(B[key] >= 2 for key in B):
            a3 = True
        if a1: 
            return "Flush"
        if a2:
            return "Three of a Kind"
        if a3:
            return "Pair"
        return "High Card"