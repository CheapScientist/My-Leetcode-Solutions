// https://leetcode.com/problems/reverse-linked-list-ii

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        for _ in range(left - 1):
            prev = prev.next
            cur = cur.next
        save = prev
        prev = None
        for _ in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        save.next.next = cur
        save.next = prev
        return dummy.next