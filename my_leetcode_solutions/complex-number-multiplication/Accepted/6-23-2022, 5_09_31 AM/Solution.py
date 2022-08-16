// https://leetcode.com/problems/complex-number-multiplication

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1List, num2List = num1.split('+'), num2.split("+")
        real1, img1 = num1List
        real2, img2 = num2List
        real1Sign = -1 if real1[0] == "-" else 1
        real2Sign = -1 if real2[0] == "-" else 1
        img1Sign = -1 if img1[0] == "-" else 1
        img2Sign = -1 if img2[0] == "-" else 1
        real1 = int(real1.lstrip("-"))
        real2 = int(real2.lstrip("-"))
        img1 = int(img1.lstrip('+').lstrip('-').rstrip('i'))
        img2 = int(img2.lstrip('+').lstrip('-').rstrip('i'))
        real, img = (real1Sign*real2Sign*real1*real2 - img1Sign*img2Sign*img1*img2), (real1Sign*real1*img2Sign*img2 + real2Sign*real2*img1Sign*img1)
        return str(real) + "+" + str(img) + "i"