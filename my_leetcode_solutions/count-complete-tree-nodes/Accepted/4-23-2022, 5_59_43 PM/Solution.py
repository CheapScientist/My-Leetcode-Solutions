// https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        ans = 1
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    ans +=1 
                    q.append(cur.left)
                if cur.right:
                    ans += 1
                    q.append(cur.right)
        return ans