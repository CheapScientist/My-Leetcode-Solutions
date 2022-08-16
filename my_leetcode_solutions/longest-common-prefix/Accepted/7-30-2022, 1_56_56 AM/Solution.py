// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for string in strs:
            if len(string) == 0:
                return ""
            trie.insert(string)
        prefix = []
        cur = trie.root
        while len(cur.children) == 1 and not cur.isWord:
            A = list(cur.children.keys())[0]
            prefix.append(A)
            cur = cur.children[A]
        return ''.join(prefix)
        
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str):
        cur = self.root
        
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isWord = True