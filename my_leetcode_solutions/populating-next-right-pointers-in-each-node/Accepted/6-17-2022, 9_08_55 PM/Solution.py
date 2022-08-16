// https://leetcode.com/problems/populating-next-right-pointers-in-each-node

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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        q = deque([root])
        while q:
            temp = []
            for _ in range(len(q)):
                cur = q.popleft()
                if cur: 
                    q.append(cur.left)
                    q.append(cur.right)
                temp.append(cur)
            if not temp: 
                continue
            if len(temp) == 1: 
                temp[0].next = None
                continue
            for i in range(1, len(temp)):
                if temp[i - 1]:
                    temp[i - 1].next = temp[i]

        return root