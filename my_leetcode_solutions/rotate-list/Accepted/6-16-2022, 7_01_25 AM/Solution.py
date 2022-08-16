// https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        l = 0
        cur = head
        while cur: 
            l += 1
            cur = cur.next
        k = k%l
        fast, slow = head, head
        for _ in range(k): 
            fast = fast.next
        while fast and fast.next: 
            fast, slow = fast.next, slow.next
        fast.next = head
        temp = slow.next
        slow.next = None
        return temp