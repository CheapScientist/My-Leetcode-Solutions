// https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, head
        for _ in range(right - left):
            fast = fast.next
        for _ in range(left - 1):
            slow = slow.next
            fast = fast.next
        tail = slow
        prev = None
        cur = tail.next
        for _ in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            cur, prev = tmp, cur
        tail.next.next = cur
        tail.next = prev
        return dummy.next
        
        
        