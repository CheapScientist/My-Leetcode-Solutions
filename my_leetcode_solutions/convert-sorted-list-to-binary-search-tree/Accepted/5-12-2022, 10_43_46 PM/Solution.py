// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        headList = []
        cur = head
        while cur:
            headList.append(cur.val)
            cur = cur.next
        
        
        def recursive(nums):
            if not nums:
                return 
            l, r = 0, len(nums) - 1
            mi = (l + r)//2
            root = TreeNode(nums[mi])
            root.left = recursive(nums[:mi])
            root.right = recursive(nums[mi + 1:])
            
            return root
        
        return recursive(headList)
        