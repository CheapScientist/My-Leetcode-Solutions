// https://leetcode.com/problems/array-nesting

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        visited = set()
        for i in range(n):
            visiting = set()
            candidate = i
            while candidate not in visited:
                visited.add(candidate)
                visiting.add(candidate)
                candidate = nums[candidate]
            res = max(res, len(visiting))
        return res
        