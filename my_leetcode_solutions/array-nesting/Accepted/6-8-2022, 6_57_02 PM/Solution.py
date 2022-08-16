// https://leetcode.com/problems/array-nesting

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        visited = set()
        for i in range(n):
            # visiting = set()
            count = 0
            candidate = i
            while candidate not in visited:
                visited.add(candidate)
                # visiting.add(candidate)
                count += 1
                candidate = nums[candidate]
            res = max(res, count)
        return res
        