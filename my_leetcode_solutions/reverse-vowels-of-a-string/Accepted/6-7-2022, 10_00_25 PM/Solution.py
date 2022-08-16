// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowelsList = []
        for i in s:
            if i in vowels:
                vowelsList.append(i)
        i = j = 0
        vowelsList = vowelsList[::-1]
        ans = []
        while i < len(s):
            char = s[i]
            if char in vowels:
                ans.append(vowelsList[j])
                j += 1
            else:
                ans.append(char)
            i += 1
        return ''.join(ans)