// https://leetcode.com/problems/robot-bounded-in-circle

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        mp = {'N':0, 'W':1, 'S':2, 'E':3}
        # 0, 1, 2, 3 -> 'N', 'W', 'S', 'E'
        def turn(init_dir: int, s: str):
            # sanity check:
            if s not in 'LR':
                return -1
            # if turning right:
            if s == 'L':
                final_dir = (init_dir + 1)%4
            else:
                final_dir = (init_dir + 3)%4
            return final_dir
        init_state = [0, 0, 0] # (x, y, dir)
        
        def move(state: list):
            x, y, direction = state
            if direction == 0: 
                return [x, y + 1]
            if direction == 1:
                return [x - 1, y]
            if direction == 2: 
                return [x, y - 1]
            if direction == 3:
                return [x + 1, y]
        final_state = init_state[:]
        for instruction in instructions: 
            # x, y, direction = ini_state
            if instruction in 'LR':
                final_state[2] = turn(final_state[2], instruction) 
                
            else:
                final_state[0], final_state[1] = move(final_state)

        x, y, direction = final_state

        if x == 0 and y == 0:
            return True
        if (x != 0 or y != 0) and direction == 0:
            return False
        return True