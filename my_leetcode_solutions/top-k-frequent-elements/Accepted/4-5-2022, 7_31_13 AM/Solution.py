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
        bucketList = bucketList[::-1]
        res, count = [], 0
        for i in bucketList:
            if i:
                res += i
                count += len(i)
            if count == k:
                break
        return res