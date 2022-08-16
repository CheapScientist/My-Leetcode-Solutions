// https://leetcode.com/problems/count-number-of-bad-pairs

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        A = []
        for i, j in enumerate(nums):
            A.append(j - i)
        memo = {}
        ans = 1 
        total = 0
        n = len(nums)
        for i in range(n - 1):
            total += ans
            ans += 1
        
        for i in A:
            if i in memo:
                total -= memo[i]
            memo[i] = memo.get(i, 0) + 1
        return total