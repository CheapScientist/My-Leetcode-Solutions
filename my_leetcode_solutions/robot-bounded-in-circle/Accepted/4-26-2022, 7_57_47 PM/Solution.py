// https://leetcode.com/problems/robot-bounded-in-circle

class Solution:
    def isRobotBounded(self, instructions: str):
        iniState = [0, 0, "N"]
        leftMap = {"N": "W", "W": "S", "S": "E", "E":"N"}
        rightMap = {}
        for i in leftMap:
            rightMap[leftMap[i]] = i
    
        def ini2Final(state, instructions):
            for i in instructions:
                if i == 'L':
                    state = left(state)
                elif i == 'R':
                    state = right(state)
                else:
                    state = forward(state)
            return state
            
        def left(state):
            state[2] = leftMap[state[2]]
            return state
        def right(state):
            state[2] = rightMap[state[2]]
            return state
        def forward(state):
            x, y, di = state
            if di == "N":
                state[1] = y + 1
            elif di == "S":
                state[1] = y - 1
            elif di == "E":
                state[0] = x + 1
            else:
                state[0] = x - 1
            return state
        
        finalState = ini2Final(iniState, instructions)
        xf, yf, directionf = finalState
        if xf == 0 and yf == 0:
            return True
        elif (xf != 0 or yf != 0) and directionf == 'N':
            return False
        else: 
            return True
            
                        
                
        