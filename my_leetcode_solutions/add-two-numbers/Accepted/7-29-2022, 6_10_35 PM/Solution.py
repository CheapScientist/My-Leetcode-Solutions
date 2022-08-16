// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1, l2
        carry = 0
        cur = ListNode()
        dummy = cur
        
        while h1 or h2: 
            val1 = h1.val if h1 else 0
            val2 = h2.val if h2 else 0
            val = val1 + val2 + carry
            carry = val//10
            val = val%10
            new = ListNode()
            new.val = val
            cur.next = new
            cur = cur.next
            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None
        if carry: 
            new = ListNode()
            new.val = carry 
            cur.next = new
        return dummy.next