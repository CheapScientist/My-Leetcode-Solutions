// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None:
            return head
        dummy = ListNode(0,head)
        prev = dummy
        cur = dummy.next
        while cur:
            if cur.next and cur.next.val == cur.val:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
                # if cur.next is None:
                #     return dummy.next
        return dummy.next