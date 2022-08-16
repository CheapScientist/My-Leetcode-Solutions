// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words) == 1: return words
        stack = [words[0]]
        i = 1
        while i < len(words):
            if sorted(words[i]) == sorted(stack[-1]):
                i += 1
            else:
                stack.append(words[i])
        return stack
        