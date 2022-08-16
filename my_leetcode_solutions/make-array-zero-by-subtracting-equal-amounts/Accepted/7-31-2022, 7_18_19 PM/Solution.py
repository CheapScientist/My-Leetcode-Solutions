// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        A = list(set([i for i in nums if i != 0]))
        return len(A)
            
        