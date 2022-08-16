// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.startStr = ''
        self.destStr = ''
        self.found1 = False
        self.found2 = False
        
        def dfs(node, path, target1, target2):
            if not node: return 
            if node.val == target1:
                self.found1 = True
                self.startStr = path
            if node.val == target2:
                self.found2 = True
                self.destStr = path
            if self.found1 and self.found2:
                return
            dfs(node.left, path +'L', target1, target2)
            dfs(node.right, path + 'R', target1, target2)
        dfs(root, '', startValue, destValue)
        ans = ''
        print(self.startStr)
        start, dest = self.startStr, self.destStr
        i = j = 0
        while i < len(start) and j < len(dest) and start[i] == dest[j]:
            i += 1
            j += 1
        ans += 'U'* (len(start) - i)
        ans += dest[i:]
        return ans
        
        