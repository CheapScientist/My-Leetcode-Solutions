// https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
            if not fast or not fast.next:
                return None
        new = dummy
        count = 0
        while new != slow:
            new = new.next
            slow = slow.next
            count += 1
        print(count)
        return new
