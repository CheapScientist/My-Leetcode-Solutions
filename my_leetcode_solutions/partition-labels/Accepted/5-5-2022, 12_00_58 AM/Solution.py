// https://leetcode.com/problems/partition-labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s: return []
        memo = {i:[] for i in range(26)}
        for i, j in enumerate(s):
            memo[ord(j) - ord('a')].append(i)
        temp = []
        for i in memo:
            if memo[i]:
                temp.append([min(memo[i]), max(memo[i])])
        temp.sort()
        if len(temp) == 1:
            return [temp[0][1] - temp[0][0] + 1]
        intervals = [temp[0]]
        for i in range(1, len(temp)):
            l, r = temp[i]
            lastl, lastr = intervals[-1]
            if l <= lastr and r > lastr:
                intervals[-1] = [lastl, r]
            elif l > lastr:
                intervals.append([l, r])
        ans = []        
        for l, r in intervals:
            ans.append((r - l + 1))
        return ans