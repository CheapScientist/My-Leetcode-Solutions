// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            lookup = [0]*26
            for j in i:
                lookup[ord(j) - ord('a')] += 1
            res[tuple(lookup)].append(i)
        return res.values()