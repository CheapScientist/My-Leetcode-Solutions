// https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # first ptr 
        j = n - 1
        k = (m + n) - 1
        while i >=0 or j >= 0:
            firstNum = nums1[i] if i >=0 else float('-inf')
            secondNum = nums2[j] if j >= 0 else float('-inf')
            if firstNum >= secondNum:
                nums1[i], nums1[k] = nums1[k], firstNum
                i -= 1
            else:
                nums2[j], nums1[k] = nums1[k], secondNum
                j -= 1
            k -= 1
        