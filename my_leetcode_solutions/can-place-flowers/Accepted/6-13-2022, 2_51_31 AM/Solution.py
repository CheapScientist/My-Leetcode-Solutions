// https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, A: List[int], nn: int) -> bool:
        if not nn: return True
        if not A: return False
        res = 0 
        i = 0
        n = len(A)
        while i < len(A):
            if A[i] == 1: 
                i += 1
            else:
                j = i + 1
                while j < len(A) and A[j] == 0: 
                    j += 1
                if i == 0 and j == n: 
                    res += (j - i + 1)//2
                elif i == 0 or j == n: 
                    res += (j - i)//2
                else:
                    res += (j - i - 1)//2
                if res >= nn:
                    return True
                i = j + 1
        return False