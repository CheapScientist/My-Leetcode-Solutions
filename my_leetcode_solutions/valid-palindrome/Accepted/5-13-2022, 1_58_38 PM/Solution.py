// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove irrelavant chars
        news = ''
        
        def helper(char):
            if (26 > ord(char) - ord('a') >=0) or (26 > ord(char) - ord('A') >=0) or 10 > ord(char) - ord('0') >= 0:
                return True, char.upper()
            else:
                return False, ''
            
        for i in s:
            a = helper(i)
            if a[0]:
                news += a[1]
        if not news: return True
        l, r = 0, len(news) - 1
 
        while l <= r :
            if news[r] != news[l]:
                return False
            l += 1
            r -= 1 
        return True
        