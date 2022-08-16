// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pointer = 0
        i = 0
        while pointer in range(len(strs[0])):
            while (i+1) in range(len(strs)):
                if strs[i][:pointer+1] != strs[i+1][:pointer+1]:
                    return strs[i][:pointer]
                else:
                    i += 1
            pointer += 1
            i = 0
        return strs[0][:pointer]