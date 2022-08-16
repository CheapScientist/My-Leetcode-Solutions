// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = [float('inf')]
        for i in nums:
            if i <= d[-1]:
                idx = bisect_left(d, i)
                d[idx] = i
            else:
                d.append(i)
                
        return len(d)