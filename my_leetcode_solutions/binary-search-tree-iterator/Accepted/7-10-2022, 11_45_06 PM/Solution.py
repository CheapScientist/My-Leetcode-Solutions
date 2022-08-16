// https://leetcode.com/problems/binary-search-tree-iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.addToStack(root)

    def next(self) -> int:
        ans_node = self.stack.pop()
        ans = ans_node.val
        # if ans_node.right:
        self.addToStack(ans_node.right)
        return ans
        
    def hasNext(self) -> bool:
        return len(self.stack) != 0
        
    def addToStack(self, cur):
        while cur:
            self.stack.append(cur)
            cur = cur.left
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()