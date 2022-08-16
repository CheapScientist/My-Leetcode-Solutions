// https://leetcode.com/problems/minimum-sum-of-squared-difference

from sortedcontainers import SortedDict
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        nums = []
        for num1, num2 in zip(nums1, nums2):
            nums.append(abs(num1-num2))
        
        k = k1 + k2
        
        count = SortedDict(Counter(nums))
        
        if k - sum(nums) >= 0:
            return 0
        
        while k > 0:
            key, value = count.popitem()
            if k >= value:
                k -= value
                if key - 1 not in count:
                    count[key-1] = value
                elif key - 1 in count:
                    count[key-1] += value
            elif k < value:
                count[key] = value - k
                if key - 1 not in count:
                    count[key-1] = k
                elif key - 1 in count:
                    count[key-1] += k
                k = 0
        
        res = 0
        for key, val in count.items():
            res += key ** 2 * val
            
        return res