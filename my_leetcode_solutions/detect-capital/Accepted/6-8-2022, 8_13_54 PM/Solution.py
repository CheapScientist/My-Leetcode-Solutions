// https://leetcode.com/problems/detect-capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if word[0].upper() == word[0]:
            cap_letter = 1
            check = True
        else:
            cap_letter = 0
            check = False
        
        for char in word[1:]: 
            if char.upper() == char: 
                cap_letter += 1
        # case 1: all cap
        if cap_letter == len(word):
            return True
        # case 2: no cap 
        if not cap_letter: 
            return True
        if cap_letter == 1 and check:
            return True
        return False