// https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return ""
        new = []
        i = 0
        while i < len(s):
            temp = []
            if s[i] == " ":
                while i + 1 < len(s) and s[i + 1] == " ":
                    i += 1
            else:
                temp = [i]
                while i + 1 < len(s) and s[i + 1] != " ":
                    i += 1
                temp.append(i)
                new.append(s[temp[0]:temp[1] + 1])
            i += 1
        new = new[::-1]
        final = ""
        for i in new:
            final += i + ' '
        return final[:-1]
                    
        