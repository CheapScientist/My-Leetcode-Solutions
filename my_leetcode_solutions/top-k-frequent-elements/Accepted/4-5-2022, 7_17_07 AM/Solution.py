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
        tpList.sort(key = lambda x: x[1], reverse = True)
        for i in range(k):
            res.append(tpList[i][0])
        return res