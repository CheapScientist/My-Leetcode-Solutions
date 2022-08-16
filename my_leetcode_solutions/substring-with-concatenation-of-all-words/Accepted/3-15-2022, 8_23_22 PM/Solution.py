// https://leetcode.com/problems/substring-with-concatenation-of-all-words

class Solution:
    def findSubstring(self, s: str, words: list[str]):
        length = len(words[0])
        l = len(words)
        cache = {}
        ans = []
        for i in words:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1
        s_ptr = 0
        substrHash = {}
        while s_ptr <= (len(s) - length*l):
            sSlice = s[s_ptr:s_ptr + length*l]
            count = 0
            for i in range(1, l+1):
                if sSlice[count:count+length] in cache and sSlice[count:count+length] not in substrHash:
                    cache[sSlice[count:count+length]] -= 1
                else:
                    substrHash[sSlice[count:count+length]] = 1
                    break
                count += length
            s_ptr += 1
            if list(cache.values()) == [0]*len(list(cache.values())):
                ans.append(s_ptr-1)
            cache = self.cacheReset(words)
        return ans

    @staticmethod
    def cacheReset(words):
        cache = {}
        for i in words:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1
        return cache