// https://leetcode.com/problems/longest-string-chain

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=lambda w: len(w))
        graph = defaultdict(set)
        for i in range(n):
            word = words[i]
            for j in range(len(word)):
                graph[word[:j]+word[j+1:]].add(i)
        dists = [1] * n
        ans = 1
        for u in range(n):
            for v in graph[words[u]]:
                dists[v] = max(dists[v], dists[u]+1)
                ans = max(ans, dists[v])
        return ans