// https://leetcode.com/problems/fizz-buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if not n: return []
        ans = [0]*(n + 1)
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans[i] = "FizzBuzz"
                continue
            elif i % 3 == 0:
                ans[i] = "Fizz"
                continue
            elif i % 5 == 0:
                ans[i] = 'Buzz'
                continue
            else:
                ans[i] = str(i)
                continue
        return ans[1:]