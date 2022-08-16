// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        idx, n = 0, len(arr)
        while idx < n:
            j = idx
            while idx + 1 < n and arr[idx + 1] == arr[idx]:
                idx += 1
            if idx - j >= n//4:
                return arr[idx]
            idx += 1
        
        return -1