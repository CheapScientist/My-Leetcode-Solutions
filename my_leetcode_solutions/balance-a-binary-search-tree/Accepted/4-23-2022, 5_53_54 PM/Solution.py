// https://leetcode.com/problems/balance-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        orderdList = []
        def BST2sort(node):
            if node:
                BST2sort(node.left)
                orderdList.append(node.val)
                BST2sort(node.right)
        def sort2BalancedTree(left, right):
            if left > right:
                return None
            else:
                mid = (left + right)//2
                newNode = TreeNode(orderdList[mid])
                newNode.left = sort2BalancedTree(left, mid - 1)
                newNode.right = sort2BalancedTree(mid + 1, right)
                return newNode
        BST2sort(root)
        ans = sort2BalancedTree(0, len(orderdList) - 1)
        return ans