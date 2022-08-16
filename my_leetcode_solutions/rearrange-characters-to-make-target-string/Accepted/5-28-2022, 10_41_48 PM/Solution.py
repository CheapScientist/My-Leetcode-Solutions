// https://leetcode.com/problems/rearrange-characters-to-make-target-string

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:

        new1 = [0]*26
        new2 = [0]*26
        for i in target: 
            new2[ord(i) - ord('a')] += 1
        for i in s:
            new1[ord(i) - ord('a')] += 1
        a1 = []
        a2 = []
        for i, j in enumerate(target):
            if new2[ord(j) - ord('a')] != 0:
                a1.append(new2[ord(j) - ord('a')])
                a2.append(new1[ord(j) - ord('a')])
        mn = float('inf')
        for i in range(len(a1)):
            mn = min(mn, a2[i]//a1[i])

        return mn if mn != float('inf') else 0
        
        