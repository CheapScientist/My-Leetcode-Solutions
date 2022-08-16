// https://leetcode.com/problems/student-attendance-record-i

class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and s.count('LLL') == 0
        
            
