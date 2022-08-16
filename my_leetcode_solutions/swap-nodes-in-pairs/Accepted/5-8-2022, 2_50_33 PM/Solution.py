// https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        if not head: return None
        if not head.next: return head
        
        prev, cur = dummy, dummy.next
        while cur and cur.next:
            snd = cur.next
            trd = cur.next.next
            cur.next = trd
            prev.next = snd
            snd.next = cur
            prev, cur = cur, trd
        
        return dummy.next