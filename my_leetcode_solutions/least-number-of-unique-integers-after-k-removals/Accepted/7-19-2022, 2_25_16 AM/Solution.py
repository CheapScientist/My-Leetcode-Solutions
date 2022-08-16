// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = {}
        for i in arr:
            count[i] = count.get(i, 0) + 1
        b = list(count.values())
        b.sort()
        n = len(b)
        print(b, k)
        for i in range(n):
            if k < b[i]:
                return n - i
            if k == b[i]:
                return n - i - 1
            k -= b[i]
        return 0