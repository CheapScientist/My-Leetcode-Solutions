// https://leetcode.com/problems/restore-ip-addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        n = len(s)
        
        def helper(s: str):
            if s == '0':
                return True
            if s.lstrip('0') != s:
                return False
            if not (256 > int(s) >=0):
                return False
            return True
        
        def dfs(s, idx, path, res):
            if idx > 4:
                return 
            if idx == 4 and not s:
                res.append(path[:-1])
                return 
            for i in range(1, len(s)+1):
                if helper(s[:i]):
                    dfs(s[i:], idx+1, path+s[:i]+".", res)
        dfs(s, 0, "", res)
        return res