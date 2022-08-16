// https://leetcode.com/problems/n-ary-tree-preorder-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        
        def dfs(node):
            if not node: return 
            ans.append(node.val)
            if node.children:
                for child in node.children:
                    dfs(child)
            
            return 
        dfs(root)
        return ans