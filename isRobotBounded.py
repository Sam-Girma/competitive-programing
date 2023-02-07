class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curr = [0,0]
        dxdy = [(0,1), (-1,0), (0,-1), (1,0)]
        direction = 0
        for inst in instructions:
            if inst == "G":
                curr = [curr[0]+dxdy[direction][0], curr[1]+dxdy[direction][1]]
            elif inst == "L":
                direction = (direction + 1) % 4
            elif inst == "R":
                if direction == 0:
                    direction = 3
                else:
                    direction = direction - 1
        
        flag_origin = curr[0] == 0 and curr[1] == 0

        return flag_origin or direction != 0
