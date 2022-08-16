// https://leetcode.com/problems/intersection-of-two-arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        set1 = set(nums1)
        for num2 in nums2:
            if num2 in set1 and num2 not in ans:
                ans.add(num2)
        return list(ans)