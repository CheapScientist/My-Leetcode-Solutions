// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         n = len(preorder)
#         memo = {}
#         for i, j in enumerate(inorder):
#             memo[j] = i
        
#         def dfs(l, r):
#             if l > r: 
#                 return None
#             self.preorder_index += 1
#             root = TreeNode(val = preorder[self.preorder_index])
#             root_inorder_index = memo[root.val]
#             root.left, root.right = dfs(l, root_inorder_index - 1), dfs(root_inorder_index + 1, r)
#             return root
#         self.preorder_index = 0
#         return dfs(0, n - 1)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def array_to_tree(left, right):
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[self.preorder_index]
            root = TreeNode(root_value)


            self.preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        self.preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)