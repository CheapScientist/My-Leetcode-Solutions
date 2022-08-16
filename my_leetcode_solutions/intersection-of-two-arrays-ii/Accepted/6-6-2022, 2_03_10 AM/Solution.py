// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        dict1 = {}
        for i in nums1: 
            dict1[i] = dict1.get(i, 0) + 1
        for j in nums2:
            if j in dict1 and dict1[j]>0:
                dict1[j] -= 1
                ans.append(j)
        return ans