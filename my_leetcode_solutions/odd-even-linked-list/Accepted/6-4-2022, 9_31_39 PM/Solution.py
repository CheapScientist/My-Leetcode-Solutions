// https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        prev, newhead, newtail = head, head.next, head.next
        while newtail and newtail.next:
            temp = newtail.next
            prev.next = temp
            newtail.next = temp.next
            temp.next = newhead
            # then shift pointers
            prev = temp
            newtail = newtail.next
        
        return dummy.next
        