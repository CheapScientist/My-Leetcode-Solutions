// https://leetcode.com/problems/array-nesting

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        # visited = set()
        for i in range(n):
            count = 0
            candidate = i
            while nums[candidate] != -1:
                temp = candidate
                count += 1
                candidate = nums[candidate]
                nums[temp] = -1
            res = max(res, count)
        return res
        