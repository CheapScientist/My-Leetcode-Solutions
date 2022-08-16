// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        
        def bsleft(nums: list[int], target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mi = (l + r)//2
                if target > nums[mi]:
                    l = mi + 1
                else:
                    r = mi - 1
            return l # will return left, inclusive
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                loc = bsleft(d, n)
                d[loc] = n
        return len(d)

