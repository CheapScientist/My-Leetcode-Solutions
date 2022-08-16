// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for string in strs: 
            ans[''.join(sorted(list(string)))] = ans.get(''.join(sorted(list(string))), []) + [string]
        return list(ans.values())
        