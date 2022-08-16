// https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # O(1) space
        # get the length of the two first
        curA, curB, lA, lB = headA, headB, 0, 0
        while curA:
            lA += 1
            curA = curA.next
        while curB:
            lB += 1
            curB = curB.next
        diff = abs(lA - lB)
        curA, curB = headA, headB
        if lA >= lB:
            for _ in range(diff):
                curA = curA.next
        else:
            for _ in range(diff):
                curB = curB.next
        while curA:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None
        