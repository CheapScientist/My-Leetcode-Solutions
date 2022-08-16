// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        def dfs(head):
            newHead = head
            if head.next:
                newHead = dfs(head.next)
                head.next.next = head
            head.next = None
            return newHead
        return dfs(head)