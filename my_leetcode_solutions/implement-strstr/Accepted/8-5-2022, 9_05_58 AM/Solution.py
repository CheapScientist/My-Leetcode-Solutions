// https://leetcode.com/problems/implement-strstr

class Solution:
    def strStr(self, s: str, p: str) -> int:
        return self.kmp(s, p)
        
    def kmp(self, s: str, p: str) -> bool:
        nxt = self.next(p)
        n, m = len(s), len(p)
        # initialize two pointers, i -> s; j -> p
        i = j = 0
        while i < n:
            # if they match:
            if s[i] == p[j]:
                i += 1
                j += 1
            elif j:
                j = nxt[j - 1]
            else:
                i += 1
            if j == m:
                return i - j
        return -1

    def next(self, p: str) -> list[int]:
         # first position is 0
        same_length = 0
        idx = 1
        n = len(p)
        ans = [0] * n
        while idx < n:
            # if they match:
            if p[idx] == p[same_length]:
                same_length += 1
                ans[idx] = same_length
                idx += 1
                continue
            # if they do not match:
            # case 1. if they do not match at all, e.g it does not even match the first element, simply skip this step:
            if not same_length:
                idx += 1
                continue
            same_length = ans[same_length - 1]
        return ans