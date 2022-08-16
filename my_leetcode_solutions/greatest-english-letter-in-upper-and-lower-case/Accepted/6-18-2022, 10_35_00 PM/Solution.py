// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case

class Solution:
    def greatestLetter(self, s: str) -> str:
        foundUpper = [False]*26
        ans = []
        foundLower = [False]*26
        for i in s: 
            # i upper
            if i.upper() == i: 
                if foundLower[ord(i.lower()) - ord('a')]: 
                    ans.append(i)
                foundUpper[ord(i.upper()) - ord('A')] = True
            else:
                if foundUpper[ord(i.upper()) - ord('A')]:
                    ans.append(i.upper())
                foundLower[ord(i.lower()) - ord('a')] = True
        return max(ans) if ans else ""