// https://leetcode.com/problems/insertion-sort-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedDummy = ListNode(-5001)
        sortedHead = sortedDummy
        while head: 
            value = head.val
            sortedHead = self.insertIntoSortedList(sortedHead, value)
            head = head.next
        return sortedDummy.next
    def insertIntoSortedList(self, sortedHead, value):
        dummy = ListNode(0, sortedHead)
        cur = dummy.next
        lastNode = ListNode(value, None)
        while cur:
            if cur.next is None:
                cur.next = lastNode
                break
            if cur.next and cur.next.val > value >= cur.val:
                lastNode.next = cur.next
                cur.next = lastNode
                break
            else:
                cur = cur.next
        return dummy.next
                