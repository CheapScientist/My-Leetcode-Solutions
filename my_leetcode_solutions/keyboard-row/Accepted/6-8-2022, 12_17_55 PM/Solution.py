// https://leetcode.com/problems/keyboard-row

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        ans = []
        for word in words:
            row1TF, row2TF, row3TF = False, False, False
            temp = word.lower()
            for char in temp:
                if char in row1:
                    row1TF = True
                elif char in row2:
                    row2TF = True
                elif char in row3:
                    row3TF = True
                else:
                    break
            if not word:
                continue
            if row1TF + row2TF + row3TF == 1:
                ans.append(word)
            else:
                continue
        return ans