// https://leetcode.com/problems/apply-discount-to-prices

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        a = sentence.split(' ')
        new = ''

        def helper(s:str):
            if s == '$':
                return False
            dollar = False
            dec = False
            num = False
            for i in s:
                if i == '$':
                    if dollar:
                        return False
                    dollar = True
                elif i in '0123456789':
                    num = True
                    if not dollar:
                        return False
                elif i == '.':
                    if dot:
                        return False
                    if not num:
                        return False
                    dot = True
                else: 
                    return False
            return True
        for i in a:
            if not helper(i):
                new += i + ' '
            else:
                c = float(i[1:])*((100 - discount)/100)
                b = f'{c:.2f}'
                new += '$' + str(b) + ' '
        ee = ''
        if new:
            ee = new[:-1]
        return ee
        
                