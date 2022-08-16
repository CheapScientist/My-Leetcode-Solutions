// https://leetcode.com/problems/relative-ranks

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        memo = {}
        for i, j in enumerate(score):
            memo[j] = i
        score.sort(reverse = True)
        ans = [0]*len(score)
        for j in range(len(score)):
            i = score[j]
            if j == 0: 
                ans[memo[i]] = "Gold Medal"
            elif j == 1: 
                ans[memo[i]] = "Silver Medal"
            elif j == 2:
                ans[memo[i]] = "Bronze Medal"
            else:
                ans[memo[i]] = str(j + 1)
        return ans
        
        