// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        power = 0
        ptr1 = l1
        ptr2 = l2
        ans = 0
        carry = 0
        while ptr1 or ptr2:
            ans1 = ptr1.val if ptr1 else 0
            ans2 = ptr2.val if ptr2 else 0
            total = ans1 + ans2 + carry 
            carry = total//10
            total = total%10
            ans += total*10**power
            # update nodes and pow
            power += 1
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next

        if carry:
            ans += 10**power
        dummy = ListNode()
        cur = dummy
        for i in str(ans)[::-1]:
            cur.next = ListNode(int(i))
            cur = cur.next
        return dummy.next