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
        while ptr1 and ptr2:
            ans1 = ptr1.val if ptr1 else 0
            ans2 = ptr2.val if ptr2 else 0
            total = ans1 + ans2 + carry 
            carry = total//10
            total = total%10
            ans += total*10**power
            
            # update nodes and pow
            power += 1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        while ptr1:
            temp = ptr1.val + carry
            carry = temp//10
            temp = temp%10
            ans += temp*10**power
            power += 1
            ptr1 = ptr1.next
        while ptr2:
            temp = ptr2.val + carry
            carry = temp//10
            temp = temp%10
            ans += temp*10**power
            power += 1
            ptr2 = ptr2.next
        if carry:
            ans += 10**power
        dummy = ListNode()
        cur = dummy
        for i in str(ans)[::-1]:
            cur.next = ListNode(int(i))
            cur = cur.next
        return dummy.next