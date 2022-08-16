// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        valandlvl = [[root.val, 0]]
        lvl = 1
        
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    valandlvl.append([cur.left.val, lvl])
                if cur.right:
                    q.append(cur.right)
                    valandlvl.append([cur.right.val, lvl])
            lvl += 1
        

        res = [valandlvl[-1]]
        for i in range(len(valandlvl) - 2, -1, -1):
            val, lvl = valandlvl[i]
            if lvl != res[-1][1]:
                res.append([val, lvl])
        ans = []
        for i in range(len(res) - 1, -1, -1):
            ans.append(res[i][0])
        return ans
                
        
        