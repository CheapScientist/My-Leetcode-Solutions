// https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return ''
        res = []
        temp = s.split()
        for i in temp: 
            res.append(i[::-1])
        return ' '.join(res)