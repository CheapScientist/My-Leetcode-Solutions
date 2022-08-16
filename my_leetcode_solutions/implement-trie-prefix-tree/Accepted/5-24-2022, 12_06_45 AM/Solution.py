// https://leetcode.com/problems/implement-trie-prefix-tree

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.wordCount = 0
        self.wordSet = set()

    def insert(self, word: str) -> None:
        cur = self.root
        if word not in self.wordSet:
            self.wordSet.add(word)
            self.wordCount += 1
            for char in word:
                if char not in cur.children:
                    new = TrieNode()
                    cur.children[char] = new
                cur = cur.children[char]
            cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        if cur.isWord:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for pref in prefix:
            if pref not in cur.children:
                return False
            cur = cur.children[pref]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)