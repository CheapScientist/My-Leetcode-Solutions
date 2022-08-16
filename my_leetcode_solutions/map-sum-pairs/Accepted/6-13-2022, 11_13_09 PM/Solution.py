// https://leetcode.com/problems/map-sum-pairs

class TreeNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = ''


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TreeNode()
            cur = cur.children[char]
        cur.isWord = True
        cur.word = word

    def searchPrefix(self, prefix: str):
        cur = self.root
        res = []
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return []

        def dfs(node):
            if node.isWord:
                res.append(node.word)
            if node.children:
                for child in node.children:
                    dfs(node.children[child])

        dfs(cur)
        return res


class MapSum:

    def __init__(self):
        self.Trie = Trie()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val
        self.Trie.insert(key)

    def sum(self, prefix: str) -> int:
        wordList = self.Trie.searchPrefix(prefix)
        ans = 0
        for word in wordList:
            if word not in self.map:
                continue
            ans += self.map[word]
        return ans