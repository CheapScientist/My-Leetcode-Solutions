// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        for s in strs: 
            b = list(s)
            b.sort()
            memo[''.join(b)] = memo.get(''.join(b), []) + [s]
        return list(memo.values())