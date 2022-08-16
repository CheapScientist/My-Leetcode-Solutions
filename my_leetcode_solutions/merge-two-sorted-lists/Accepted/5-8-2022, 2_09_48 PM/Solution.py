// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        newHead = ListNode()
        dummy.next = newHead
        ptr1, ptr2 = list1, list2
        while ptr1 or ptr2:
            val1 = ptr1.val if ptr1 else 101
            val2 = ptr2.val if ptr2 else 101
            if val1 >= val2:
                newHead.next = ListNode(val2)
                ptr2 = ptr2.next
            else:
                newHead.next = ListNode(val1)
                ptr1 = ptr1.next
            newHead = newHead.next
        return dummy.next.next
        