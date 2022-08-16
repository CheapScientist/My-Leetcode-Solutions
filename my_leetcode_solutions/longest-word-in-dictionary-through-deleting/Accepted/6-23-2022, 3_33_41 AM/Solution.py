// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        n = len(s)
        
        def dfs(i, j, word): # i -> s, j -> word; n -> len(s), m -> len(word)
            m = len(word)
            if j == m: 
                return True
            if i == n:
                return False

            if s[i] == word[j]: 
                return dfs(i + 1, j + 1, word)
            else:
                return dfs(i + 1, j, word)
            
        res = ""
        length = 0
        for word in dictionary: 
            if dfs(0, 0, word): 
                if res: 
                    if len(word) > length:
                        res = word
                        length = len(word)
                    elif len(word) == length:
                        res = min(res, word)
                else:
                    length = len(word)
                    res = word
        return res
        