// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = {}
        for i, j in enumerate(numbers):
            if (target - j) in lookup:
                return lookup[target - j] + [i+1]
            if j not in lookup:
                lookup[j] = [i+1]
