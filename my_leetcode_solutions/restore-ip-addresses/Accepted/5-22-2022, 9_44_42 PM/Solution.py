// https://leetcode.com/problems/restore-ip-addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = set()
        path = []
        n = len(s)
        
        def helper(s: str):
            if not s:
                return False
            if s == '0':
                return True
            if s.lstrip('0') != s:
                return False
            if not (256 > int(s) >=0):
                return False
            return True
        
        def dfs(s: str, nn: int):
            if nn == 0 and not s:
                temp = ''
                for i in path[:]:
                    temp += i + '.'
                res.add(temp[:-1])
                return True
            for j in range(1, n):
                if helper(s[:j]):
                    path.append(s[:j])
                    dfs(s[j:], nn - 1)
                    path.pop()
            return 
        dfs(s, 4)
        return list(res)