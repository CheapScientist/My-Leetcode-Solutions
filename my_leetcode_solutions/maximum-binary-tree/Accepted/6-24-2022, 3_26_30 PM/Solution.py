// https://leetcode.com/problems/maximum-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def get_max(l, r) -> int: # [inclusive, inclusive]
            mx = float('-inf')
            for i in range(l, r + 1):
                if nums[i] > mx: 
                    mx = nums[i]
                    idx = i
            return idx
        
        def dfs(l, r): 
            if l > r: return None
            newNode = TreeNode()
            mx_idx = get_max(l, r)
            newNode.val = nums[mx_idx]
            newNode.left, newNode.right = dfs(l, mx_idx - 1), dfs(mx_idx + 1, r)
            return newNode
        return dfs(0, len(nums) - 1)