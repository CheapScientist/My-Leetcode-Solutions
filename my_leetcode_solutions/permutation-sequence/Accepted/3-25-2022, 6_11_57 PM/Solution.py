// https://leetcode.com/problems/permutation-sequence

class Solution:
    def getPermutation(self, n, k):
        nlist = list(range(1, n + 1))
        ans = self.permute(nlist, k-1)
        return ans

    def permute(self, nlist, k):
        l = len(nlist)
        if l == 1:
            return str(nlist[0])
        else:
            f = self.fact(l - 1)
            first_num = nlist[k//f]
            remainingSortedList = [c for c in nlist if c != first_num]
            return str(first_num) + self.permute(remainingSortedList, k % f)

    def fact(self, k):
        if k == 1:
            return 1
        else:
            return k*self.fact(k-1)