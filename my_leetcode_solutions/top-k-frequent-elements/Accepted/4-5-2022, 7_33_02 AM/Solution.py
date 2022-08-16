// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        bucketList = [[] for i in range(len(nums) + 1)]
        for i in h:
            bucketList[h[i]].append(i)
        res, count = [], 0
        for i in range(len(bucketList) - 1, -1, -1):
            if bucketList[i]:
                res += bucketList[i]
                count += len(bucketList[i])
            if count == k:
                break
        return res