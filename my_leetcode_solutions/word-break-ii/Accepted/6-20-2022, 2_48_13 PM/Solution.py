// https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word = set(wordDict)
        n = len(s)
        ans = []
        build = []
        
        def dfs(i): 
            if i >= n: 
                ans.append(' '.join(build))
                return
            for j in range(i, n): 
                temp = s[i:j+1]
                if temp in word:
                    build.append(temp)
                    dfs(j + 1)
                    build.pop()
            return 
        dfs(0)
        return ans