// https://leetcode.com/problems/decode-the-message

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = ''.join(key.split(' '))
        seen = [False]*26
        key1 = ''
        for i in key: 
            if not seen[ord(i) - ord('a')]:
                seen[ord(i) - ord('a')] = True
                key1 += i
        mp = {}
        for i in range(26):
            mp[key1[i]] = chr(ord('a')+i)

        ans = []
        for i in message:
            if i == ' ': 
                ans.append(i)
            else:
                ans.append(mp[i])
        return ''.join(ans)