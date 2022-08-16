// https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        if head.next == None:
            return head
        dummy = ListNode(0, head)
        length = 0
        while dummy.next:
            dummy = dummy.next
            length += 1
        k = k%length
        dummy = ListNode(0, head)
        prev = dummy
        curr = dummy.next
        for i in range(length - k - 1):
            curr = curr.next
        copy = curr
        nodeList = []
        for i in range(k):
            A = copy.next
            nodeList.append(A)
            copy = A
        curr.next = None
        for i in range(k):
            node = nodeList.pop()
            node.next = prev.next
            prev.next = node
        return dummy.next