// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        tpList, res = [], []
        for i in h:
            tpList.append((i, h[i]))

        for i in range(k):
            ans, tpList = self.helper(tpList)
            res.append(ans)
        return res

    def helper(self, tpList):
        mx, idx, ans = 0, -1, -1
        for j, i in enumerate(tpList):
            if i[1] > mx:
                idx = j
                mx = i[1]
                ans = i[0]
        tpList.pop(idx)
        return ans, tpList