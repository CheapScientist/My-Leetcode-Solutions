// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        res = []
        for i, j in enumerate(nums):
            if j in hash:
                res.append(hash[j])
                res.append(i)
                return res
            else:
                hash[target - j] = i
        return res