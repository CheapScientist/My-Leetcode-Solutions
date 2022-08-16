// https://leetcode.com/problems/reorder-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        if not fast:
            return head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now the first half starts from head to slow (inclusive), 
        # the second half starts from slow.next to tail
        
        # now reverse the second half
        prev = None
        cur = slow.next
        slow.next = None
        while cur: 
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        
        # now merge the two
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
