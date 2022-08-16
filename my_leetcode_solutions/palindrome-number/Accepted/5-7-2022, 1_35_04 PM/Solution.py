// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l, r = 0, len(x) - 1
        while l <= r:
            if x[r] != x[l]:
                return False
            r -= 1
            l += 1
        return True