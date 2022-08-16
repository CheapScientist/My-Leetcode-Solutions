// https://leetcode.com/problems/partition-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        right = ListNode()
        left_ln, right_ln = left, right
        cur = head
        while cur:
            if cur.val < x:
                left_ln.next = cur
                left_ln = left_ln.next 
            else:
                right_ln.next = cur
                right_ln = right_ln.next
            cur = cur.next
        left_ln.next = right.next
        right_ln.next = None
        return left.next