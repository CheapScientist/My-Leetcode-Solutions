// https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = dummy.next
        while curr and curr.next:
            nextPair = curr.next.next
            secondNode = curr.next
            curr.next = nextPair
            secondNode.next = curr
            prev.next = secondNode
            
            prev = curr
            curr = nextPair
        return dummy.next