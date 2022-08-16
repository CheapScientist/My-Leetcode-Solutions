// https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # O(n) space
        memo = set()
        cur = headA
        while cur:
            memo.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in memo:
                return cur
            cur = cur.next
        return None
        
        