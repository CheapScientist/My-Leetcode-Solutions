// https://leetcode.com/problems/count-collisions-on-a-road

class Solution:
    def countCollisions(self, directions: str) -> int:
        if not directions: return 0
        ans = 0
        stationary = False
        left, right = 0, 0
        for i in directions:
            if i == 'S':
                stationary = True
                left = 0
                if right:
                    ans += right 
                    right = 0
            elif i == 'L':
                    left += 1
                    if stationary:
                        ans += 1
                        left -= 1
                        stationary = True

                    if right:
                        ans += min(right, left)*2
                        a = min(right, left)
                        right -= a
                        left -= a
                        right = max(0, right)
                        left = max(0, left)
                        stationary = True
                        if right: 
                            ans += right
                            right = 0
                    else:
                        left = 0


            else:
                right += 1
                stationary = False
                
        return ans
                    