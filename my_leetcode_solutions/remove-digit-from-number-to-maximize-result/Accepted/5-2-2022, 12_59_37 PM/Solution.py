// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        temp = []
        for i in range(len(number) - 1):
            if number[i] == digit:
                temp.append(int(number[:i]+number[i+1:]))
        if number[-1] == digit:
            temp.append(int(number[:-1]))
        return str(max(temp))
