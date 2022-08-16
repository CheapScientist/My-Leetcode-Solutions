// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge2Lists(list1, list2):
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
        
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None