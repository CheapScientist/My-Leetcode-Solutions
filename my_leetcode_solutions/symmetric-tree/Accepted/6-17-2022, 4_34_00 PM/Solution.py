// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        q = deque([root])
        while q:
            temp = []
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left: 
                    temp.append(cur.left.val)
                    q.append(cur.left)
                else:
                    temp.append('N')
                if cur.right:
                    temp.append(cur.right.val)
                    q.append(cur.right)
                else:
                    temp.append('N')
            if temp != temp[::-1]: return False
        return True