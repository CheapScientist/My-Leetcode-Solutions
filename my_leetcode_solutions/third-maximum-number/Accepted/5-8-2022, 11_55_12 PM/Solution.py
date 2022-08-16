// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n, T = list(set(nums)), [float('-inf')]*3
        for i in n:
            if i > T[0]:
                T = [i,T[0],T[1]]
            elif i > T[1]:
                T = [T[0],i,T[1]]
            elif i > T[2]:
                T = [T[0],T[1],i]
        if T[2] != float('-inf'):
            return T[2]
        else:
            return T[0]