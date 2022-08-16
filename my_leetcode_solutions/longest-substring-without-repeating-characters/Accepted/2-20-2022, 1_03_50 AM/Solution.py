// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = []
        maxLen = 0
        for i in s:
            if i not in hash:
                hash.append(i)
            else:
                hashIdx = hash.index(i)
                hash = hash[hashIdx + 1:]
                hash.append(i)
            maxLen = max(maxLen, len(hash))
            print(hash, maxLen)
        return maxLen