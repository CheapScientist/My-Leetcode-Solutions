// https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode()
        cur = dummy.next = head
        prev = dummy
        while cur: 
            if cur.val == val: 
                temp = cur.next
                prev.next = temp
                cur = temp
            else:
                prev = cur
                cur = cur.next
                
        return dummy.next