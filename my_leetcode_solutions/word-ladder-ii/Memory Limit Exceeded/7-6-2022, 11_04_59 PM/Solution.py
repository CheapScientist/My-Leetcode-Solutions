// https://leetcode.com/problems/word-ladder-ii

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        if endWord not in wordList: return []
        lookup = defaultdict(list)
        for word in wordList:
            n = len(word)
            for i in range(n):
                temp = word[:i] + '*' + word[i + 1:]
                lookup[temp].append(word)
        visit = set()
        q = deque([(beginWord, [])])
        res = []

        while q:
            tmp = []
            cpy = []
            for i in range(len(q)):
                cur, path = q.popleft()
                if cur in visit:
                    continue
                if cur == endWord:
                    tmp.append(path + [endWord])
                cpy.append(cur)
                m = len(cur)
                for i in range(m):
                    temp = cur[:i] + '*' + cur[i + 1:]
                    if temp not in lookup:
                        continue
                    for neighbor in lookup[temp]:
                        if neighbor not in visit:
                            q.append((neighbor, path + [cur]))
            for i in cpy:
                visit.add(i)
            if tmp:
                return tmp

        return []