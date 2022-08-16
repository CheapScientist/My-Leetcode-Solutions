// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        q = deque([root])
        while q:
            temp = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    temp.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                    temp.append(cur.right)
            if not temp:
                continue
            for i in range(len(temp) - 1):
                temp[i].next = temp[i + 1]
        return root