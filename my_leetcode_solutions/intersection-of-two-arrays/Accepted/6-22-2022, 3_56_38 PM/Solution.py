// https://leetcode.com/problems/intersection-of-two-arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo = {}
        for num in nums1: 
            memo[num] = memo.get(num, 0) + 1
        ans = set()
        for num in nums2: 
            if num in memo and memo[num]: 
                ans.add(num)
                memo[num] -= 1
        return list(ans)