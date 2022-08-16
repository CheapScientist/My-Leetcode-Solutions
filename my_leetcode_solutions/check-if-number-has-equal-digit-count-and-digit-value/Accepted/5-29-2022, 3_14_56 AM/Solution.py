// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value

class Solution:
    def digitCount(self, num: str) -> bool:
        a = Counter(num)

        for i, j in enumerate(num):

            if a[str(i)] != int(j):
                return False
        return True
        
        