// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recursive(l, r):
            if l == r:
                return None
            mi = (l + r)//2
            root = TreeNode(nums[mi])
            root.left = recursive(l, mi)
            root.right = recursive(mi + 1, r)
            return root
        return recursive(0, len(nums))
        
        