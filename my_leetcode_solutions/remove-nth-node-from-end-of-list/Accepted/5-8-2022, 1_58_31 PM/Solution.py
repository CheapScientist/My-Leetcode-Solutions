// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not n: return head
        dummy = ListNode()
        dummy.next = head
        
        fast, slow = dummy, dummy
        # fisrt part is to move the fast ptr k steps
        for _ in range(n):
            fast = fast.next
        # second part is to move fast and slow together until fast.next is None
        while fast.next:
            fast = fast.next
            slow = slow.next
        # up to here we have the slow ptr pointing at the node before the one we wish to remove
        # to remove it:
        slow.next = slow.next.next
        
        return dummy.next