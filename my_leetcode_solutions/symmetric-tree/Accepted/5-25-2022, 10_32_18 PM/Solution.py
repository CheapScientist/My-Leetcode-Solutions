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
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    temp.append(cur.left.val)
                else:
                    temp.append(None)
                if cur.right:
                    q.append(cur.right)
                    temp.append(cur.right.val)
                else:
                    temp.append(None)
            if not (temp == temp[::-1]):
                return False
        
        return True
        
        