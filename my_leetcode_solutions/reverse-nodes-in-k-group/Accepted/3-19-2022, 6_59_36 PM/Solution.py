// https://leetcode.com/problems/reverse-nodes-in-k-group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        dummy = ListNode(0, head)
        prev = dummy
        curr = dummy.next
        while curr:
            temp_curr = curr
            mi_node_list = []
            for i in range(k):
                mi_node_list.append(temp_curr)
                nextCurr = temp_curr.next
                temp_curr = nextCurr
            mi_node_list[0].next = temp_curr
            for i in range(1, k):
                 mi_node_list[i].next =  mi_node_list[i-1]
            prev.next =  mi_node_list[-1]
            # update ptrs
            prev = curr
            curr = temp_curr
            curr_copy = curr
            for i in range(k):
                if nextCurr is None:
                    return dummy.next
                nextCurr = curr_copy.next
                curr_copy = nextCurr
        return dummy.next