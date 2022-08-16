// https://leetcode.com/problems/word-ladder

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        lookup = defaultdict(list)
        for word in wordList: 
            n = len(word)
            for i in range(n): 
                temp = word[:i] + '*' + word[i + 1:]
                lookup[temp].append(word)
        visit = set()
        q = deque([beginWord])
        ans = 1

        while q:
            for i in range(len(q)): 
                cur = q.popleft()
                if cur in visit:
                    continue
                if cur == endWord: 
                    return ans
                visit.add(cur)
                m = len(cur)
                for i in range(m): 
                    temp = cur[:i] + '*' + cur[i + 1:]
                    if temp not in lookup:
                        continue
                    for neighbor in lookup[temp]: 
                        if neighbor not in visit: 
                            q.append(neighbor)
            ans += 1
        return 0