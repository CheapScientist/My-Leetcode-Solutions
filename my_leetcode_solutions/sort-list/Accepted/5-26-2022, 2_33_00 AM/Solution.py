// https://leetcode.com/problems/sort-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        cur = head
        while cur:
            ans.append(cur.val)
            cur = cur.next
        ans.sort()
        dummy = ListNode()
        prev = dummy
        # print(ans)
        for i in ans:
            new = ListNode(i)
            prev.next = new
            prev = new
        return dummy.next
        