// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in s.lower():
            if 25 >= (ord(i) - ord('a')) >= 0 or i in '0123456789':
                res += i
        l, r = 0, len(res) - 1
        while l <= r:
            if res[l] != res[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
        