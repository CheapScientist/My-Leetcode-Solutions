// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            l, r = intervals[i]
            lastl, lastr = ans[-1]
            if l <= lastr and r > lastr:
                ans[-1] = [lastl, r]
            elif l > lastr:
                ans.append([l, r])
        return ans