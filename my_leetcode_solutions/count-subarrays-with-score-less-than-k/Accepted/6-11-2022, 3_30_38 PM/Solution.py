// https://leetcode.com/problems/count-subarrays-with-score-less-than-k

class Solution:
    def countSubarrays(self, A: List[int], k: int) -> int:
        res = cur = i = 0
        for j in range(len(A)):
            cur += A[j]
            while cur * (j - i + 1) >= k:
                cur -= A[i]
                i += 1
            res += j - i + 1
        return res