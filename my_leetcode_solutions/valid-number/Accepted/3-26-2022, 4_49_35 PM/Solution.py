// https://leetcode.com/problems/valid-number

class Solution:
    def isNumber(self, s: str) -> bool:
        signs = '+-'
        Es = 'eE'
        dots = '.'
        nums = '0123456789'
        adict = {}
        for i in s:
            if i not in (signs + nums + Es + dots):
                return False
            elif i in Es:
                if 'e' in adict:
                    adict['e'] += 1
                else:
                    adict['e'] = 1
            else:
                if i in adict:
                    adict[i] += 1
                else:
                    adict[i] = 1
        if 'e' in s and  adict['e'] > 1:
            return False
        if '.' in s and adict[dots] > 1:
            return False
        s = s.lower()
        if 'e' in s:
            splitS = s.split('e')
            left, right = splitS[0], splitS[1]
            if len(splitS) > 2:
                return False
            isLeftValid = self.isInteger(left) or self.isDecimal(left)
            isRightValid = self.isInteger(right)
            if isLeftValid and isRightValid:
                return True
            else:
                return False
        else:
            return self.isInteger(s) or self.isDecimal(s)

    def isInteger(self, s:str):
        signs = '+-'
        nums = '0123456789'
        sList = list(s)[::-1]
        ansStack = []
        if not s:
            return False
        while sList:
            curChar = sList.pop()
            if curChar in signs:
                for i in ansStack:
                    if i in signs:
                        return False
                if len(sList) == 0:
                    return False
                if len(ansStack) > 0:
                    return False
                ansStack.append(curChar)
            elif curChar not in (signs + nums):
                return False
            else:
                ansStack.append(curChar)
        return True
    def isIntegerWoSigns(self, s:str):
        nums = '0123456789'
        if not s:
            return False
        for i in s:
            if i not in nums:
                return False
        return True

    def isDecimal(self, s:str):
        splitS = s.split('.')
        if '.' not in s:
            return False
        if not s:
            return False
        left, right = splitS[0], splitS[1]
        if len(splitS) > 2:
            return False
        isLeftInt = self.isInteger(left)
        isRightIntWosigns = self.isIntegerWoSigns(right)
        if isLeftInt and isRightIntWosigns:
            return True
        elif isLeftInt and right == '':
            return True
        elif left == '' and isRightIntWosigns:
            return True
        elif left in '+-' and isRightIntWosigns:
            return True
        else:
            return False