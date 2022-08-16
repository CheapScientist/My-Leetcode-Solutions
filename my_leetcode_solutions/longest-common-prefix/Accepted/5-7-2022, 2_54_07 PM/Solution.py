// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for string in strs:
            if len(string) == 0:
                return ""
            trie.insert(string)
        prefix = ''
        cur = trie.root
        while len(cur.children) == 1 and not cur.isWord:
            prefix += list(cur.children.keys())[0]
            cur = cur.children[prefix[-1]]
        return prefix
        
        
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
        
    # def longestPrefix(self):       
    #     current = self.root
    #     prefix = ''
    #     while len(current.children) == 1 and not current.isWord:
    #         prefix += list(current.children.keys())[0]
    #         current = current.children[prefix[-1]]
    #     return prefix

        