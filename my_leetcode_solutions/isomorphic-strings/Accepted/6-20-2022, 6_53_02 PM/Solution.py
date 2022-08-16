// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup = {} # map {char1: char2} e.g {"p":"t"}
        i = j = 0
        lookup2 = {}
        while i < len(s):
            char1, char2 = s[i], t[j]
            if char1 not in lookup: 
                lookup[char1] = char2
            else:
                if lookup[char1] != char2: return False
            if char2 not in lookup2: 
                lookup2[char2] = char1
            else:
                if lookup2[char2] != char1: return False
            i += 1
            j += 1
        return True
    