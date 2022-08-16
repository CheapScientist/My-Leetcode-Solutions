// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head 
        s = ''
        while cur:
            s += str(cur.val)
            cur = cur.next
        power = 0
        res = 0
        for i in s[::-1]:
            res += int(i)*2**power
            power += 1
        return res