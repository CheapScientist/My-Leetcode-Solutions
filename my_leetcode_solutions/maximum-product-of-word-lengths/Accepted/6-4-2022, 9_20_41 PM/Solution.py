// https://leetcode.com/problems/maximum-product-of-word-lengths

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        memo = []
        
        def count(s:str):
            lookup = [0]*26
            for i in s:
                lookup[ord(i) - ord('a')] += 1
            return lookup
        
        def helper(l1, l2):
            n = 26
            for i in range(26):
                w1, w2 = l1[i], l2[i]
                if w1 and w2:
                    return False
            return True
        
        for i in range(n):
            word = words[i]
            memo.append(count(word))
        ans = 0
        for i in range(n):
            for j in range(1 + i, n):
                if helper(memo[i], memo[j]):
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans