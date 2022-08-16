// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        if l == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        elif l == 0:
            dummy = ListNode()
            return dummy.next
        elif l == 1:
            return lists[0]
        else:
            return self.mergeTwoLists(lists[0], self.mergeKLists(lists[1:]))
        
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
        while list1:
            cur.next = list1
            list1 = list1.next
            cur = cur.next
        while list2:
            cur.next = list2
            list2 = list2.next
            cur = cur.next
        return dummy.next