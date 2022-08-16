// https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(' ')
        ans  =[ ]
        for i in a[::-1]:
            if i: 
                ans.append(i)
        return ' '.join(ans)