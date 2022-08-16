// https://leetcode.com/problems/implement-strstr

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        n_len = len(needle)
        for i in range(len(haystack) - n_len + 1):
            a = haystack[i:i + n_len]
            if a == needle:
                return i
        return -1