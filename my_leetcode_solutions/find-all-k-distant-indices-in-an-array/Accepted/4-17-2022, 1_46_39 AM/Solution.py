// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keyList = []
        res = []
        for i, j in enumerate(nums):
            if j == key:
                keyList.append(i)
        for ii, jj in enumerate(nums):
            for kk in keyList:
                if abs(ii - kk) <= k:
                    res.append(ii)
        return list(set(res))