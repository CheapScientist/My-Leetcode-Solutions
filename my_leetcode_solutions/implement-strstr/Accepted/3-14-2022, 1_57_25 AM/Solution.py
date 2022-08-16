// https://leetcode.com/problems/implement-strstr

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(needle) == 1:
            if needle in haystack:
                return haystack.find(needle)
            else:
                return -1
        h_lptr = 0
        h_rptr = len(needle) - 1
        n_lptr = 0
        n_rptr = len(needle) - 1
        while h_lptr < h_rptr and h_rptr in range(len(haystack)):
            if haystack[h_lptr] == needle[n_lptr] and haystack[h_rptr] == needle[n_rptr]:
                h_rptr -= 1
                n_rptr -= 1
            else:
                h_lptr += 1
                h_rptr = h_lptr + len(needle) - 1
                n_rptr = len(needle) - 1
            if n_lptr >= n_rptr:
                return h_lptr
        return -1