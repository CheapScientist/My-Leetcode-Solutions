// https://leetcode.com/problems/binary-search-tree-iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.traversal = []
        cur = self.root
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.traversal.append(node.val)
            dfs(node.right)
        dfs(root)
        self.pointer = 0

    def next(self) -> int:
        ans = self.traversal[self.pointer]
        self.pointer += 1
        return ans
        
    def hasNext(self) -> bool:
        return self.pointer < len(self.traversal)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()