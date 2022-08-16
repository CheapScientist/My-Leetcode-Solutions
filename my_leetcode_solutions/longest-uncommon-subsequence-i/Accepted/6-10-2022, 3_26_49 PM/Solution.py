// https://leetcode.com/problems/longest-uncommon-subsequence-i

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1
        