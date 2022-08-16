// https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # memo is a dict that maps the old to the new
        if not head: return None
        memo = {}
        cur = head
        prev = Node(0)
        dummy = prev
        # first construct all the new nodes
        while cur: 
            newNode = Node(cur.val)
            memo[cur] = newNode
            prev.next = newNode
            prev, cur = newNode, cur.next
        
        # then point the random pointer
        cur = head
        prev = dummy.next
        while cur: 
            rdm = cur.random
            if rdm:
                prev.random = memo[rdm]
            else:
                prev.random = None
            prev, cur = prev.next, cur.next
        return dummy.next