// https://leetcode.com/problems/sender-with-largest-word-count

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        memo = {}
        mx = 0
        ans = senders[0]
        for message, sender in zip(messages, senders):
            if sender in memo:
                memo[sender] += len(message.split())
            else:
                memo[sender] = len(message.split())
            if memo[sender] > mx:
                mx = memo[sender]
                ans = sender
            elif memo[sender] == mx:
                ans = max(ans, sender)
        return ans
        