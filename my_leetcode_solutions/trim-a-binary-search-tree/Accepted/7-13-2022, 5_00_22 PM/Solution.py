// https://leetcode.com/problems/trim-a-binary-search-tree

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        
        def dfs(node):
            if not node: return None
            newNode = TreeNode()
            left, right = dfs(node.left), dfs(node.right)
            if high >= node.val >= low: 
                newNode.val = node.val
                newNode.left, newNode.right = left, right
            else:
                newNode = left or right
            return newNode
        return dfs(root)