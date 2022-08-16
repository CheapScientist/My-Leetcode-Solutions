// https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        dummy1 = left = ListNode(0)
        dummy2 = right = ListNode(0)
        count = 1
        cur = head
        while cur: 
            if count % 2: 
                left.next = cur
                left = left.next
            else:
                right.next = cur
                right = right.next
            cur = cur.next
            count += 1
        right.next = None
        left.next = dummy2.next
        return dummy1.next