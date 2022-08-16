// https://leetcode.com/problems/bulls-and-cows

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counter = [0]*10
        bulls = 0
        cows = 0
        for i in secret:
            counter[int(i)] += 1
        seen = set()
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                counter[int(secret[i])] -= 1
                seen.add(i)
        for i in range(len(secret)):
            if i not in seen and counter[int(guess[i])] > 0:
                cows += 1
                counter[int(guess[i])] -= 1
        ans = str(bulls) + 'A' + str(cows) + 'B'
        return ans