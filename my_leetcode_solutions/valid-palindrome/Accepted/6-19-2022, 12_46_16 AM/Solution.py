// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = []
        for i in s: 
            if i.isalnum():
                ans.append(i.lower())
        if not ans:
            return True
        a = ''.join(ans)
        return True if a == a[::-1] else False