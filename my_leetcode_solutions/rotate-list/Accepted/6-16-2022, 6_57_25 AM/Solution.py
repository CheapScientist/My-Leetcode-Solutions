// https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        memo = []
        cur = head
        while cur: 
            memo.append(cur)
            cur = cur.next
        k = k%len(memo)
        memo = memo[-k:] + memo[:-k]
        dummy = ListNode()
        cur = dummy
        for i in memo:
            cur.next = i
            cur = cur.next
        cur.next = None
        return dummy.next
        