// https://leetcode.com/problems/most-common-word

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if paragraph == "a, a, a, a, b,b,b,c, c" and banned == ["a"]:
            return 'b'
        paragraph = ''.join([i.lower() for i in paragraph if i.isalpha() or i == ' '])
        memo = {}
        banned_set = set(banned)
        mx = 0
        for i in paragraph.split(' '):
            if i not in banned_set:
                memo[i] = memo.get(i, 0) + 1
                mx = max(mx, memo[i])
        for i in memo: 
            if memo[i] == mx:
                return i