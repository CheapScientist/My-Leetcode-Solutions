// https://leetcode.com/problems/construct-the-rectangle

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mi = int(area**0.5)
        for i in range(mi, 0, -1):
            if area%i == 0:
                return [area//i, i]
        