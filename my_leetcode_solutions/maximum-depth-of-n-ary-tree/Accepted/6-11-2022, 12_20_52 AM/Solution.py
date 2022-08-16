// https://leetcode.com/problems/maximum-depth-of-n-ary-tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        q = deque([root])
        height = 0
        while q: 
            for i in range(len(q)):
                cur = q.popleft()
                for child in cur.children: 
                    q.append(child)
            height += 1
        return height