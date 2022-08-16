// https://leetcode.com/problems/valid-triangle-number

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) <= 2: return 0
        n = len(nums)
        a= sorted(nums)
        count = 0
        for i in range(n):
            for j in range(i+1, n-1):
                k = bisect_left(a, a[i] + a[j], lo = j+1)
                count += k - j - 1
        return count
        