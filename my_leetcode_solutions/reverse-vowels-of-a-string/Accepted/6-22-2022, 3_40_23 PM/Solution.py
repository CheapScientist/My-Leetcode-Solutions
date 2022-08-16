// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        vl = []
        for i in s: 
            if i in vowels: 
                vl.append(i)
        vl = vl[::-1]
        k = 0
        ans = []
        for i in range(len(s)):
            char = s[i]
            if char in vowels: 
                ans.append(vl[k])
                k += 1
            else:
                ans.append(char)
        return ''.join(ans)